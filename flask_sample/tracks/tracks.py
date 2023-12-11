from flask import Blueprint, flash, render_template, request, redirect, url_for
from sql.db import DB  # Import your DB class
from tracks.forms import TrackForm, TrackSearchForm, PlaylistForm  # Import your StockForm class
from roles.permissions import admin_permission, user_permission, manager_permission
from flask_login import login_user, login_required, logout_user, current_user

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
@manager_permission.require(http_exception=403)
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

    args = {}
    allowed_columns = ["title", "title_short", "duration", "track_rank", "artist_name", "album_name", "created", "modified"]
    search = request.args.get("search")
    title = request.args.get("title")
    title_short = request.args.get("title_short")
    duration = request.args.get("duration")
    artist_name = request.args.get("artist")
    album_name = request.args.get("album_name")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    page = request.args.get("page", 1, type=int)

    if search:
        query += " AND (IS601_Tracks.title LIKE %(search)s OR IS601_Tracks.artist_name LIKE %(search)s OR IS601_Tracks.album_name LIKE %(search)s)"
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
        query += " AND IS601_Tracks.album_name LIKE %(album_name)s"
        args["album_name"] = f"%{album_name}%"

    if column and order:
        if column in allowed_columns and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"
    per_page = 10
    try:
        if limit:
            limit = int(limit)
            if not 1 <= limit <= 100:
                flash("Limit must be between 1 and 100", "danger")
                has_error = True
            else:
                offset = (page - 1) * per_page
                query += " LIMIT %(offset)s, %(limit)s"
                args["offset"] = offset
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

    print(len(rows))
    total_rows = len(rows)
    
    total_pages = (total_rows + per_page - 1) // per_page

    page = request.args.get("page", 1, type=int)

    # Slice the rows based on the current page
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    rows_to_display = rows[start_index:end_index]

    return render_template("tracks_list.html", rows=rows_to_display, total_pages=total_pages, current_page=page, total_rows=total_rows)


@tracks.route("/delete", methods=["GET"])
@admin_permission.require(http_exception=403)
def delete():
    id = request.args.get("playlist_id")
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
        return redirect(url_for("tracks.list"))
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

@tracks.route("/add_playlist", methods=["GET", "POST"])
@user_permission.require(http_exception=403)
@login_required
def add_playlist():
    form = PlaylistForm()
    if form.validate_on_submit():
        print(form.data)
        try:
            # Create a new track record in the database
            result = DB.insertOne(
                "INSERT INTO IS601_Playlists (name, picture) VALUES (%s, %s)",
                form.name.data, form.picture.data
            )
            if result.status:
                flash(f"Created Playlist for {form.name.data}", "success")
                last_insert_query = "SELECT LAST_INSERT_ID() AS last_id"
                last_id_result = DB.selectOne(last_insert_query)

                if last_id_result.status and last_id_result.row:
                    playlist_id = last_id_result.row['last_id']
                    user_playlist_result = DB.insertOne(
                        "INSERT INTO IS601_UserPlaylists (user_id, playlist_id) VALUES (%s, %s)",
                        current_user.id, playlist_id
                    )

                    if not user_playlist_result.status:
                        flash("Failed to add playlist to user's playlists", "danger")
                else:
                    flash("Failed to fetch last inserted ID", "danger")
        except Exception as e:
            flash(f"Error Playlist: {e}", "danger")
    return render_template("playlist_form.html", form=form, type="Create")

#Bhavya Shah
#7th December, 2023
@tracks.route("/list_playlist", methods=["GET", "POST"])
@user_permission.require(http_exception=403)
@login_required
def list_playlist():
    rows = []
    track_id = request.args.get("id")
    has_error = False
    search = request.args.get("search")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    query = """
    SELECT p.name as 'Name', p.id as 'ID', p.picture as 'Picture' 
    FROM IS601_Playlists p
    JOIN IS601_UserPlaylists up ON p.id = up.playlist_id
    WHERE up.user_id = %(user_id)s
"""

    args = {"user_id": current_user.id}

    if search:
        query += " AND name LIKE %(search)s"
        args["search"] = f"%{search}%"

    allowed_columns = ["name", "created", "modified"]
    if column and order:
        if column in allowed_columns and order in ["asc", "desc"]:
            query += f" ORDER BY p.{column} {order}"

    # Example logic for filtering
    
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
        flash("Error getting playlist records", "danger")

    return render_template("playlist_list.html", rows=rows, track_id=track_id, username = current_user.username)


@tracks.route("/add_to_playlist", methods=["GET"])
@user_permission.require(http_exception=403)
@login_required
def add_to_playlist():
    track_id = request.args.get("track_id")
    playlist_id = request.args.get("playlist_id")
    #print(track_id)
    #print(playlist_id)
    if not track_id:
        flash("Add a song", "info")
        return redirect(url_for("tracks.list"))

    try:
        # Insert the record into the IS601_PlaylistTracks table
        result = DB.insertOne(
            "INSERT INTO IS601_PlaylistTracks (playlist_id, track_id, tracks) VALUES (%s, %s, 1) ON DUPLICATE KEY UPDATE tracks = tracks + 1",
            playlist_id, track_id
        )

        if result.status:
            flash("Added track to playlist", "success")
        else:
            flash("Failed to add track to playlist", "danger")


    except Exception as e:
        flash(f"Error adding track to playlist: {e}", "danger")

    return redirect(url_for("tracks.list_playlist"))

#Bhavya Shah
#7 December 2023
@tracks.route("/view_playlist", methods=["GET"])
@login_required
def view_playlist():
    playlist_id = request.args.get("id")
    print("View: ",playlist_id)
    if playlist_id is None:
        flash("Missing Playlist ID", "danger")
        return redirect(url_for("tracks.list_playlist"))

    try:
        # Fetch playlist information
        playlist_result = DB.selectOne(
            "SELECT name as 'Name', id as 'ID' FROM IS601_Playlists WHERE id = %s",
            playlist_id
        )
        print(playlist_result)
        if not playlist_result.status or not playlist_result.row:
            flash("Playlist not found", "danger")
            return redirect(url_for("tracks.list_playlist"))

        playlist_name = playlist_result.row["Name"]
        print(playlist_name)
        # Fetch tracks associated with the playlist
        tracks_result = DB.selectAll(
            """
            SELECT t.id as 'ID', t.track_id as 'Track ID', t.readable as 'Readable', t.title as 'Name',
                   t.title_short as 'Short Name', t.track_link as 'Track Link', t.duration as 'Duration',
                   t.track_rank as 'Ranking', t.artist_name as 'Artist', t.album_name as 'Album'
            FROM IS601_PlaylistTracks pt
            JOIN IS601_Tracks t ON pt.track_id = t.id
            WHERE pt.playlist_id = %s
            """,
            playlist_id
        )

        if tracks_result.status:
            tracks = tracks_result.rows
        else:
            tracks = []

        return render_template("playlist_view.html", playlist=playlist_name, playlist_id=playlist_id, tracks=tracks)

    except Exception as e:
        flash(f"Error fetching playlist information: {e}", "danger")
        return redirect(url_for("tracks.list_playlist"))
    
@tracks.route("/edit_playlist", methods=["GET", "POST"])
@user_permission.require(http_exception=403)
@login_required
def edit_playlist():
    playlist_id = request.args.get("id")
    form = PlaylistForm()

    if playlist_id is None:
        flash("Missing Playlist ID", "danger")
        return redirect(url_for("tracks.list_playlist"))

    try:
        # Fetch current playlist name and picture
        playlist_result = DB.selectOne(
            "SELECT name, picture FROM IS601_Playlists WHERE id = %s",
            playlist_id
        )

        if not playlist_result.status or not playlist_result.row:
            flash("Playlist not found", "danger")
            return redirect(url_for("tracks.list_playlist"))

        playlist_name = playlist_result.row["name"]
        playlist_picture = playlist_result.row["picture"]

        if form.validate_on_submit():
            # Update playlist name and picture link in the database
            try:
                result = DB.insertOne(
                    "UPDATE IS601_Playlists SET name = %s, picture = %s WHERE id = %s",
                    form.name.data, form.picture.data, playlist_id
                )

                if result.status:
                    flash(f"Updated playlist information", "success")
                    return redirect(url_for("tracks.list_playlist"))
                else:
                    flash("Failed to update playlist information", "danger")
            except Exception as e:
                flash(f"Error updating playlist information: {e}", "danger")

        # Pre-fill the form with the current playlist information
        form.name.data = playlist_name
        form.picture.data = playlist_picture

    except Exception as e:
        flash(f"Error fetching playlist information: {e}", "danger")
        return redirect(url_for("tracks.list_playlist"))

    return render_template("playlist_form.html", form=form, type="Edit Playlist")

@tracks.route("/remove_from_playlist", methods=["GET", "POST"])
@login_required
def remove_from_playlist():
    track_id = request.args.get("track_id")
    playlist_id = request.args.get("playlist_id")

    print(playlist_id)
    if not track_id or not playlist_id:
        flash("Invalid request", "danger")
        return redirect(url_for("tracks.list_playlist"))

    try:
        # Remove the track from the playlist
        result = DB.delete(
            "DELETE FROM IS601_PlaylistTracks WHERE playlist_id = %s AND track_id = %s",
            playlist_id, track_id
        )

        if result.status:
            flash("Removed track from playlist", "success")
        else:
            flash("Failed to remove track from playlist", "danger")

    except Exception as e:
        flash(f"Error removing track from playlist: {e}", "danger")

    # Check if the current user is an admin
    if admin_permission.can():
        # Redirect to the admin page
        return redirect(url_for("tracks.list_users"))
    else:
        # Redirect to the user's playlist page
        return redirect(url_for("tracks.list_playlist"))

@tracks.route("/delete_playlist", methods=["GET", "POST"])
@user_permission.require(http_exception=403)
@login_required
def delete_playlist():
    playlist_id = request.args.get("playlist_id")
    args = {**request.args}

    if not playlist_id:
        flash("Invalid request", "danger")
        return redirect(url_for("tracks.list_playlist"))

    try:
        # Fetch user playlist relation
        user_playlist_result = DB.selectOne(
            "SELECT user_id FROM IS601_UserPlaylists WHERE playlist_id = %s",
            playlist_id
        )

        if user_playlist_result.status and user_playlist_result.row:
            user_id = user_playlist_result.row['user_id']

            # Remove all tracks associated with the playlist
            result_remove_tracks = DB.delete(
                "DELETE FROM IS601_PlaylistTracks WHERE playlist_id = %s",
                playlist_id
            )

            if result_remove_tracks.status:
                # Delete user playlist relation
                result_remove_user_playlist = DB.delete(
                    "DELETE FROM IS601_UserPlaylists WHERE playlist_id = %s",
                    playlist_id
                )

                if result_remove_user_playlist.status:
                    # Tracks removed successfully, user playlist relation removed, now delete the playlist
                    result_delete_playlist = DB.delete(
                        "DELETE FROM IS601_Playlists WHERE id = %s",
                        playlist_id
                    )

                    if result_delete_playlist.status:
                        flash("Deleted playlist and removed all tracks", "success")
                    else:
                        flash("Failed to delete playlist", "danger")
                else:
                    flash("Failed to remove user playlist relation", "danger")
            else:
                flash("Failed to remove tracks from the playlist", "danger")
        else:
            flash("User playlist relation not found", "danger")

    except Exception as e:
        flash(f"Error deleting playlist: {e}", "danger")

    return redirect(url_for("tracks.list_playlist", **args))

@tracks.route("/list_users", methods=["GET"])
@admin_permission.require(http_exception=403)
def list_users():
    try:
        # Fetch a list of users from your database
        users_result = DB.selectAll(
            "SELECT id, username, email FROM IS601_Users"
        )

        if users_result.status and users_result.rows:
            users = users_result.rows
            return render_template("list_users.html", users=users)
        else:
            flash("No users found", "warning")

    except Exception as e:
        flash(f"Error fetching user list: {e}", "danger")

    return redirect(url_for("tracks.list"))

@tracks.route("/view_user", methods=["GET"])
@admin_permission.require(http_exception=403)
def view_user():
    user_id = request.args.get("user_id")

    if user_id is None:
        flash("Missing user ID", "danger")
        return redirect(url_for("tracks.list_users"))

    try:
        # Fetch user details from your database
        user_result = DB.selectOne(
            "SELECT id, username, email FROM IS601_Users WHERE id = %s",
            user_id
        )

        if user_result.status and user_result.row:
            user = user_result.row
            return render_template("view_user.html", user=user)
        else:
            flash("User not found", "danger")

    except Exception as e:
        flash(f"Error fetching user details: {e}", "danger")

    return redirect(url_for("tracks.list_users"))


@tracks.route("/user_playlists", methods=["GET"])
@admin_permission.require(http_exception=403)
def user_playlists():
    user_id = request.args.get("user_id")

    if user_id is None:
        flash("Missing user ID", "danger")
        return redirect(url_for("tracks.list_users"))

    try:
        # Fetch user details from your database
        user_result = DB.selectOne(
            "SELECT id, username, email FROM IS601_Users WHERE id = %s",
            user_id
        )

        if not user_result.status or not user_result.row:
            flash("User not found", "danger")
            return redirect(url_for("tracks.list_users"))

        user = user_result.row

        # Fetch playlists associated with the user
        playlists_result = DB.selectAll(
            """
            SELECT p.name as 'Name', p.id as 'ID', p.picture as 'Picture' 
            FROM IS601_Playlists p
            JOIN IS601_UserPlaylists up ON p.id = up.playlist_id
            WHERE up.user_id = %s
            """,
            user_id
        )

        if playlists_result.status:
            playlists = playlists_result.rows
        else:
            playlists = []

        return render_template("user_playlists.html", user=user, playlists=playlists)

    except Exception as e:
        flash(f"Error fetching user playlists: {e}", "danger")

    return redirect(url_for("tracks.list_users"))

@tracks.route("/clear_user_associations", methods=["GET", "POST"])
@user_permission.require(http_exception=403)
@login_required
def clear_user_playlists():
    user_id = request.args.get("user_id")
    args = {**request.args}

    if not user_id:
        flash("Invalid request", "danger")
        return redirect(url_for("tracks.list_playlist"))

    try:
        # Fetch all playlist IDs for the user
        user_playlists_result = DB.selectAll(
            "SELECT playlist_id FROM IS601_UserPlaylists WHERE user_id = %s",
            user_id
        )

        if user_playlists_result.status and user_playlists_result.rows:
            playlist_ids = [playlist['playlist_id'] for playlist in user_playlists_result.rows]

            # Remove all tracks associated with the playlists
            for playlist_id in playlist_ids:
                result_remove_tracks = DB.delete(
                    "DELETE FROM IS601_PlaylistTracks WHERE playlist_id = %s",
                    playlist_id
                )

                if not result_remove_tracks.status:
                    flash(f"Failed to remove tracks from playlist {playlist_id}", "danger")

            # Delete user playlist relations
            result_remove_user_playlists = DB.delete(
                "DELETE FROM IS601_UserPlaylists WHERE user_id = %s",
                user_id
            )

            if result_remove_user_playlists.status:
                flash("Cleared all playlists for the user", "success")
            else:
                flash("Failed to clear user playlists", "danger")

        else:
            flash("No playlists found for the user", "danger")

    except Exception as e:
        flash(f"Error clearing user playlists: {e}", "danger")

    return redirect(url_for("tracks.list_playlist", **args))


@tracks.route("/list_tracks_in_user_playlists", methods=["GET"])
@admin_permission.require(http_exception=403)
def list_tracks_in_user_playlists():
    tracks = []
    has_error = False

    # Your database query to fetch tracks in user playlists
    query = """
    SELECT t.id, t.track_id, t.title as Name,t.duration as Duration, t.artist_name as Artist, t.track_rank as Ranking, t.album_name as Album, COUNT(u.id) AS UsersCount
    FROM IS601_Tracks t
    LEFT JOIN IS601_PlaylistTracks pt ON t.id = pt.track_id
    LEFT JOIN IS601_Playlists p ON pt.playlist_id = p.id
    LEFT JOIN IS601_UserPlaylists up ON p.id = up.playlist_id
    LEFT JOIN IS601_Users u ON up.user_id = u.id
    GROUP BY t.id, t.track_id, t.title, t.artist_name, t.album_name
    """

    args = {}  # Add any additional query parameters here
    search = request.args.get("search")
    column = request.args.get("column")
    order = request.args.get("order")
    user_count_filter = request.args.get("user_count")
     # Apply search filter
    
    if search:
        query += " HAVING LOWER(t.title) LIKE LOWER(%(search)s)"
        args["search"] = f"%{search}%"

    # Apply UserCount filter
    
    if user_count_filter is not None and user_count_filter.isdigit():
        user_count_filter = int(user_count_filter)
        query += " HAVING UsersCount = %(user_count_filter)s"
        args["user_count_filter"] = user_count_filter
    # Apply sortin  # Default sorting order is ascending

    # Ensure the sort column is valid to prevent SQL injection
    valid_sort_columns = ["Name", "Duration", "Artist", "Album", "Ranking", "UsersCount"]
    if column not in valid_sort_columns:
        #flash("Invalid sort column", "danger")
        has_error = True
    else:
        query = f"""
            SELECT * FROM (
                {query}
            ) AS subquery
            ORDER BY {column} {order}
        """

    # Apply limit
    limit = request.args.get("limit", 10)
    try:
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
            tracks = result.rows
            print(tracks)
    except Exception as e:
        print(e)
        flash("Error getting tracks in user playlists", "danger")

    return render_template("list_tracks_in_user_playlists.html", rows=tracks)


@tracks.route("/admin_add_to_playlist", methods=["GET"])
@admin_permission.require(http_exception=403)
@login_required
def admin_add_to_playlist():
    track_id = request.args.get("track_id")
    playlist_id = request.args.get("playlist_id")
    user_id = request.args.get("user_id")
    print("Playlist ID:", playlist_id)
    if not track_id:
        flash("Add a song", "info")
        return redirect(url_for("tracks.list", user_id=user_id, playlist_id=playlist_id))

    try:
        # Insert the record into the IS601_PlaylistTracks table
        result = DB.insertOne(
            "INSERT INTO IS601_PlaylistTracks (playlist_id, track_id, tracks) VALUES (%s, %s, 1) ON DUPLICATE KEY UPDATE tracks = tracks + 1",
            playlist_id, track_id
        )

        if result.status:
            flash("Added track to playlist", "success")
        else:
            flash("Failed to add track to playlist", "danger")


    except Exception as e:
        flash(f"Error adding track to playlist: {e}", "danger")

    return redirect(url_for("tracks.user_playlists", user_id=user_id))

