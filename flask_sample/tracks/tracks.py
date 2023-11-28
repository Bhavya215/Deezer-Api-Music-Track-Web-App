from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB  # Import your DB class
from tracks.forms import TrackForm, TrackSearchForm  # Import your StockForm class
from roles.permissions import admin_permission

tracks = Blueprint('tracks', __name__, url_prefix='/tracks', template_folder='templates')

#Bhavya Shah - bs635
#26 November, 2023
@tracks.route("/fetch", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def fetch():
    i=1
    t_id = None
    form = TrackSearchForm()
    if form.validate_on_submit():
        try:
            from utils.Deezer import Deezer
            from utils.lazy import DictToObject
            # Create a new stock record in the database
            result = Deezer.search(form.q.data)
            if result:
                #print(result)
                for i in range(0,10):
                    resp = result["data"][i]
                    res = DictToObject(resp)
                    #print(resp)
                    t_id = DB.selectOne("""Select track_id from IS601_Tracks WHERE track_id = %s""", res.id)
                    print(t_id.row)
                    if t_id.row is None:
                        print("Exit")
                        break
                #print(resp)
                result = DictToObject(resp)
                artist = DictToObject(result.artist)
                album = DictToObject(result.album)
                result = DB.insertOne(
                    """INSERT INTO IS601_Tracks (track_id, readable, title, title_short, track_link, duration, track_rank, artist_name, album_name)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                        track_id = VALUES(track_id),
                        readable = VALUES(readable),
                        title = VALUES(title),
                        title_short = VALUES(title_short),
                        track_link = VALUES(track_link),
                        duration = VALUES(duration),
                        track_rank = VALUES(track_rank),
                        artist_name = VALUES(artist_name),
                        album_name = VALUES(album_name)""",
                    result.id, result.readable, result.title, result.title_short, result.link, result.duration, result.rank, artist.name, album.title
                )
                if result.status:
                    flash(f"Loaded Track record for {form.q.data}", "success")
        except Exception as e:
            flash(f"Error loading Track record: {e}", "danger")
    return render_template("track_search.html", form=form)

#Bhavya Shah - bs635
#26 November, 2023
@tracks.route("/add", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def add():
    form = TrackForm()
    if form.validate_on_submit():
        print(form.data)
        try:
            # Create a new track record in the database
            result = DB.insertOne(
                "INSERT INTO IS601_Tracks (track_id, readable, title, title_short, track_link, duration, track_rank, artist_name, album_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                form.track_id.data, form.readable.data, form.title.data, form.title_short.data, form.track_link.data, form.duration.data, form.track_rank.data, form.artist_name.data, form.album_name.data
            )
            if result.status:
                flash(f"Created track record for {form.title.data}", "success")
        except Exception as e:
            flash(f"Error creating track record: {e}", "danger")
    return render_template("track_form.html", form=form, type="Create")

@tracks.route("/edit", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def edit():
    form = TrackForm()
    id = request.args.get("id")
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("tracks.list"))
    if form.validate_on_submit() and id:
        try:
            # Update the existing stock record in the database
            result = DB.insertOne(
                "UPDATE IS601_Tracks SET track_id = %s, readable = %s, title = %s, title_short = %s, track_link = %s, duration = %s, track_rank = %s, artist_name = %s, album_name = %s WHERE id = %s",
                form.track_id.data, form.readable.data, form.title.data, form.title_short.data, form.track_link.data, form.duration.data, form.track_rank.data, form.artist_name.data, form.album_name.data, id
            )
            if result.status:
                flash(f"Updated track record for {form.title.data}", "success")
        except Exception as e:
            flash(f"Error updating track record: {e}", "danger")
    try:
        result = DB.selectOne(
            "SELECT track_id, readable, title, title_short, track_link, duration, track_rank, artist_name, album_name FROM IS601_Tracks WHERE id = %s",
            id
        )
        if result.status and result.row:
            form = TrackForm(data=result.row)
    except Exception as e:
        flash("Error fetching track record", "danger")
    return render_template("track_form.html", form=form, type="Edit")

@tracks.route("/list", methods=["GET"])

def list():
    rows = []
    has_error = False

    query = "SELECT title as 'Name', title_short as 'Short Name', track_link as 'Track Link', duration as 'Duration', artist_name as 'Artist', album_name as 'Album', track_rank as 'Ranking', id as 'ID', track_id as 'Track ID', readable FROM IS601_Tracks WHERE 1=1"

    args = {}  # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["title", "title_short", "duration", "track_rank", "artist_name", "album_name", "created", "modified"]
    track_id = request.args.get("id")
    search = request.args.get("search")
    title = request.args.get("title")
    title_short = request.args.get("title_short")
    duration = request.args.get("duration")
    artist_name = request.args.get("artist")
    album_name = request.args.get("album_name")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    print(search)
    if search:
        query += " AND IS601_Tracks.title LIKE %(search)s OR IS601_Tracks.artist_name LIKE %(search)s OR IS601_Tracks.album_name LIKE %(search)s"
        args["search"] = f"%{search}%"

    if title:
        query += " AND IS601_Tracks.title LIKE %(title)s"
        args["title"] = f"%{title}%"

    
    if title_short:
        query += " AND IS601_Tracks.title_short LIKE %(title_short)s"
        args["title_short"] = f"%{title_short}%"

    
    if duration:
        query += " AND IS601_Tracks.duration LIKE %(duration)s"
        args["duration"] = f"%{duration}%"

    
    if artist_name:
        query += " AND IS601_Tracks.artist_name LIKE %(artist_name)s"
        args["artist_name"] = f"%{artist_name}%"

    
    if album_name:
        query += " AND al.title LIKE %(album_name)s"
        args["album_name"] = f"%{album_name}%"

    
    if column and order:
        if column in allowed_columns and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"

    
    try:
        if limit:
            limit = int(limit)
            if not 1 <= limit <= 100:
                flash("Limit must be between 1 and 100", "danger")
                has_error = True
            else:
                query += " LIMIT %(limit)s"
                args["limit"] = limit
    
    except ValueError:
        flash("Limit must be a number", "danger")
        has_error = True

    try:
        result = DB.selectAll(query, args)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print(e)
        flash("Error getting track records", "danger")
    return render_template("tracks_list.html", rows=rows)

@tracks.route("/delete", methods=["GET"])
@admin_permission.require(http_exception=403)
def delete():
    id = request.args.get("id")
    args = {**request.args}
    if id:
        try:
            # Delete the track record from the database
            result = DB.delete("DELETE FROM IS601_Tracks WHERE id = %s", id)
            if result.status:
                flash("Deleted track record", "success")
        except Exception as e:
            flash(f"Error deleting track record: {e}", "danger")
        del args["id"]
    else:
        flash("No ID present", "warning")
    return redirect(url_for("tracks.list", **args))

@tracks.route("/view", methods=["GET"])

def view():
    id = request.args.get("id")
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("stocks.list"))
    try:
        result = DB.selectOne(
            "SELECT  id as 'ID', track_id as 'Track ID', readable as 'Readable', title as 'Name', title_short as 'Short Name', track_link as 'Track Link' , duration as 'Duration', track_rank as 'Ranking' , artist_name as 'Artist', album_name as 'Album' FROM IS601_Tracks WHERE id = %s",
            id
        )
        if result.status and result.row:
            print(result.row)
            return render_template("track_view.html", track=result.row)
        else:
            flash("Track record not found", "danger")
    except Exception as e:
        print(f"Track error {e}")
        flash("Error fetching Track record", "danger")
    return redirect(url_for("tracks.list"))