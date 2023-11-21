from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB

import pycountry
organization = Blueprint('organization', __name__, url_prefix='/organization')

@organization.route("/search", methods=["GET"])
def search():
    rows = []
    organization_id = request.args.get("organization_id")
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, donation count as donations for the organization
    # don't do SELECT * and replace the below "..." portion
    
    query = """
        SELECT
            IS601_MP3_Organizations.name as name, 
            IS601_MP3_Organizations.address as address, 
            IS601_MP3_Organizations.city as city, 
            IS601_MP3_Organizations.country as country, 
            IS601_MP3_Organizations.state as state, 
            IS601_MP3_Organizations.zip as zip, 
            IS601_MP3_Organizations.website as website,
            (SELECT COUNT(*) FROM IS601_MP3_Donations WHERE IS601_MP3_Donations.organization_id = IS601_MP3_Organizations.id) as donations,
            IS601_MP3_Organizations.id
        FROM
            IS601_MP3_Organizations
        WHERE 1=1
    """
    args = {}  # <--- add values to replace %s/%(named)s placeholders

    
    # TODO search-2 get name, country, state, column, order, limit request args
    # TODO search-3 append a LIKE filter for name if provided
    # TODO search-4 append an equality filter for country if provided
    # TODO search-5 append an equality filter for state if provided
    # TODO search-6 append sorting if column and order are provided and within the allows columns and allowed order asc,desc
    # TODO search-7 append limit (default 10) or limit greater than or equal to 1 and less than or equal to 100
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    # TODO search-2 get name, country, state, column, order, limit request args
    allowed_columns = ["name", "city", "country", "state", "modified", "created"]
    name = request.args.get("name")
    city = request.args.get("city")
    country = request.args.get("country")
    state = request.args.get("state")
    column = request.args.get("column")
    order = request.args.get("order")

    # TODO search-3 append a LIKE filter for name if provided
    if name:
        query += " AND name LIKE %(name)s"
        args["name"] = f"%{name}%"

    # TODO search-4 append an equality filter for country if provided
    if country:
        query += " AND country = %(country)s"
        args["country"] = country

    # TODO search-5 append an equality filter for state if provided
    if state:
        query += " AND state = %(state)s"
        args["state"] = state

    # TODO search-6 append sorting if column and order are provided and within the allows columns and allowed order asc,desc
    if column and column in allowed_columns and order in ["asc", "desc"]:
        query += f" ORDER BY {column} {order}"

    # TODO search-7 append limit (default 10) or limit greater than or equal to 1 and less than or equal to 100
    try:
        limit = int(request.args.get("limit", 10))
        if 1 <= limit <= 100:
            query += " LIMIT %(limit)s"
            args["limit"] = limit
        else:
            raise ValueError("Limit must be between 1 and 100")
    except ValueError:
        # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
        flash("Invalid limit value. Please provide a number between 1 and 100.", "danger")

    try:
        result = DB.selectAll(query, args)
        print(f"result {result.rows}")
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-9 make message user-friendly
        flash(str(e), "danger")

    # hint: use allowed_columns in the template to generate the sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    #sort_options = [(col, col.capitalize()) for col in allowed_columns]

    return render_template("list_organizations.html", rows=rows, allowed_columns=allowed_columns)

@organization.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        has_error = False # use this to control whether or not an insert occurs
        
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website, description
        # TODO add-2 name is required (flash proper error message)
        # TODO add-3 address is required (flash proper error message)
        # TODO add-4 city is required (flash proper error message)
        # TODO add-5 state is required (flash proper error message)
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation to solve this
        # TODO add-6 country is required (flash proper error message)
        # TODO add-6a country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation to solve this
        # TODO add-7 website is not required
        # TODO add-8 zip is required (flash proper error message)
        # note: call zip variable zipcode as zip is a built in function it could lead to issues
        # TODO add-9 description is not required

        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website, description
        name = request.form.get("name")
        description = request.form.get("description", "")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        zip_code = request.form.get("zip")
        website = request.form.get("website", "")
        print(address)
        print(city)

        # TODO add-2 name is required (flash proper error message)
        if not name:
            flash("Organization Name is required", "danger")
            has_error = True

        # TODO add-3 address is required (flash proper error message)
        if not address:
            flash("Address is required", "danger")
            has_error = True

        # TODO add-4 city is required (flash proper error message)
        if not city:
            flash("City is required", "danger")
            has_error = True
        
        state1 = country + "-" + state

        # TODO add-5 state is required (flash proper error message)
        if not state:
            flash("State is required", "danger")
            has_error = True
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        elif state1 not in [s.code for s in pycountry.subdivisions.get(country_code=country) ]:
            flash("Invalid State", "danger")
            has_error = True

        # TODO add-6 country is required (flash proper error message)
        if not country:
            flash("Country is required", "danger")
            has_error = True
        # TODO add-6a country should be a valid country mentioned in pycountry
        elif country not in [c.alpha_2 for c in pycountry.countries]:
            flash("Invalid Country", "danger")
            has_error = True

        # TODO add-7 website is not required

        # TODO add-8 zip is required (flash proper error message)
        if not zip_code:
            flash("Zip Code is required", "danger")
            has_error = True

        # TODO add-9 description is not required


        if not has_error:
            try:
                result = DB.insertOne("""
                    INSERT INTO IS601_MP3_Organizations (name, description, address, city, state, country, zip, website)
                    VALUES (%(name)s, %(description)s, %(address)s, %(city)s, %(state)s, %(country)s, %(zip)s, %(website)s)
                """, {
                    "name": name,
                    "description": description,
                    "address": address,
                    "city": city,
                    "state": state,
                    "country": country,
                    "zip": zip_code,
                    "website": website
                })
                if result.status:
                    flash("Added Organization", "success")
            except Exception as e:
                # TODO add-11 make message user-friendly
                flash("An error occurred while adding the organization. Please try again later.", "danger")
        
    return render_template("manage_organization.html", org=request.form)

@organization.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id")
    if not id:
        flash("Organization ID is required.", "danger")
        # Redirect or handle the error as needed
        return redirect(url_for("organization.search"))

    if request.method == "POST":
        data = {"id": id}  # use this as needed, can convert to tuple if necessary
        # TODO edit-2 retrieve form data for name, address, city, state, country, zip, website
        name = request.form.get("name")
        description = request.form.get("description")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        zip_code = request.form.get("zip")
        website = request.form.get("website")

        # TODO edit-3 name is required (flash proper error message)
        if not name:
            flash("Name is required.", "danger")
            return redirect(url_for("organization.edit", id=id))

        # TODO edit-4 address is required (flash proper error message)
        if not address:
            flash("Address is required.", "danger")
            return redirect(url_for("organization.edit", id=id))

        # TODO edit-5 city is required (flash proper error message)
        if not city:
            flash("City is required.", "danger")
            return redirect(url_for("organization.edit", id=id))

        # TODO edit-6 state is required (flash proper error message)
        if not state:
            flash("State is required.", "danger")
            return redirect(url_for("organization.edit", id=id))

        # TODO edit-6a state should be a valid state mentioned in pycountry for the selected state
        valid_states = [subdivision.code.split("-")[1] for subdivision in pycountry.subdivisions.get(country_code=country, default=[])]
        if state not in valid_states:
            flash("Invalid state selected.", "danger")
            return redirect(url_for("organization.edit", id=id))

        # TODO edit-7 country is required (flash proper error message)
        if not country:
            flash("Country is required.", "danger")
            return redirect(url_for("organization.edit", id=id))

        # TODO edit-7a country should be a valid country mentioned in pycountry
        valid_countries = [country.alpha_2 for country in pycountry.countries]
        if country not in valid_countries:
            flash("Invalid country selected.", "danger")
            return redirect(url_for("organization.edit", id=id))

        # TODO edit-8 website is not required
        # TODO edit-9 zipcode is required (flash proper error message)
        if not zip_code:
            flash("Zip Code is required.", "danger")
            return redirect(url_for("organization.edit", id=id))

        # note: call zip variable zipcode as zip is a built-in function it could lead to issues

        # populate data dict with mappings
        data.update({
            "name": name,
            "description": description,
            "address": address,
            "city": city,
            "state": state,
            "country": country,
            "zip": zip_code,
            "website": website
        })

        has_error = False  # use this to control whether or not an insert occurs

        if not has_error:
            try:
                # TODO edit-10 fill in the proper update query
                # name, address, city, state, country, zip, website
                result = DB.update("""
                UPDATE IS601_MP3_Organizations
                SET
                    name = %(name)s,
                    description = %(description)s,
                    address = %(address)s,
                    city = %(city)s,
                    state = %(state)s,
                    country = %(country)s,
                    zip = %(zip)s,
                    website = %(website)s
                WHERE
                    id = %(id)s
                """, data)

                if result.status:
                    flash("Updated record", "success")
            except Exception as e:
                # TODO edit-11 make this user-friendly
                print(f"{e}")
                flash(str(e), "danger")

    row = {}
    try:
        # TODO edit-12 fetch the updated data
        result = DB.selectOne("""
        SELECT
            id, name, description, address, city, state, country, zip, website, created, modified
        FROM
            IS601_MP3_Organizations
        WHERE
            id = %(id)s
        """, {"id": id})
        if result.status:
            row = result.row

    except Exception as e:
        # TODO edit-13 make this user-friendly
        flash("An error occurred while fetching the organization details. Please try again.", "danger")

    return render_template("manage_organization.html", org=row)

@organization.route("/delete", methods=["GET"])
def delete():
    # TODO delete-4 pass all argument except id to this route
    id = request.args.get("id")
    print(id)
    # TODO delete-1 if id is missing, flash necessary message and redirect to search
    if not id:
        flash("Organization ID is missing. Please provide a valid organization ID.", "danger")
        return redirect(url_for("organization.search"))

    try:
        # TODO delete-2 delete organization by id
        # Note: You may need to trigger a delete of all donations related to this organization first
        # due to foreign key constraints. Adjust the code accordingly.
        result = DB.delete("DELETE FROM IS601_MP3_Organizations WHERE id = %s", id)

        if result.status:
            # TODO delete-3 ensure a flash message shows for successful delete
            flash("Organization deleted successfully.", "success")
        else:
            # TODO delete-3 ensure a flash message shows for unsuccessful delete
            flash("Failed to delete organization. Please try again.", "danger")

    except Exception as e:
        # TODO delete-3 ensure a flash message shows for unsuccessful delete
        flash("An error occurred while deleting the organization. Please try again.", "danger")

    # TODO delete-5 redirect to organization search
    return redirect(url_for("organization.search"))