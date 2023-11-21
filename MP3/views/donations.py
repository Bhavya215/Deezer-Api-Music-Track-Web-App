from datetime import datetime, timedelta
from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
donations = Blueprint('donations', __name__, url_prefix='/donations')

import re

def is_valid_email(email):
    # A basic regex pattern for email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

@donations.route("/search", methods=["GET"])
def search():
    rows = []
    organization_name = ""
    has_error = False
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve donation id as id, donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments, organization_name using a LEFT JOIN
    #Bhavya Shah 19 November, 2023
    query = """
        SELECT  IS601_MP3_Donations.donor_firstname as 'Donor Firstname',
                IS601_MP3_Donations.donor_lastname as 'Donor Lastname',
                IS601_MP3_Donations.donor_email as 'Donor Email',
                IS601_MP3_Donations.item_name as 'Item Name',
                IS601_MP3_Donations.item_description as 'Item Description',
                IS601_MP3_Donations.item_quantity as 'Item Quantity',
                IS601_MP3_Donations.donation_date as 'Donation Date',
                IS601_MP3_Donations.comments as Comments,
                IS601_MP3_Organizations.name AS organization_name,
                IS601_MP3_Donations.created as created,
                IS601_MP3_Donations.modified as modified
        FROM IS601_MP3_Donations
        LEFT JOIN IS601_MP3_Organizations ON IS601_MP3_Donations.organization_id = IS601_MP3_Organizations.id
        WHERE 1=1
    """
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["donor_firstname", "donor_lastname", "donor_email", "organization_name" ,"item_name", "item_quantity", "created", "modified"]
    # TODO search-2 get fn, ln, email, organization_id, column, order, limit from request args
    fn = request.args.get("fn")
    ln = request.args.get("ln")
    email = request.args.get("email")
    item_name = request.args.get("item_name")
    organization_id = request.args.get("organization_id")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)

    # TODO search-3 append like filter for donor_firstname if provided
    #Bhavya Shah 19 November, 2023
    if fn:
        query += " AND IS601_MP3_Donations.donor_firstname LIKE %(donor_firstname)s"
        args["donor_firstname"] = f"%{fn}%"

    # TODO search-4 append like filter for donor_lastname if provided
    #Bhavya Shah 19 November, 2023
    if ln:
        query += " AND IS601_MP3_Donations.donor_lastname LIKE %(donor_lastname)s"
        args["donor_lastname"] = f"%{ln}%"

    # TODO search-5 append like filter for donor_email if provided
    #Bhavya Shah 19 November, 2023
    if email:
        query += " AND IS601_MP3_Donations.donor_email LIKE %(donor_email)s"
        args["donor_email"] = f"%{email}%"
    
    # TODO search-6 append like filter for item_name if provided
    #Bhavya Shah 19 November, 2023
    if item_name:
        query += " AND IS601_MP3_Donations.item_name LIKE %(item_name)s"
        args["item_name"] = f"%{item_name}%"

    # TODO search-7 append equality filter for organization_id if provided
    #Bhavya Shah 19 November, 2023
    if organization_id:
        query += " AND IS601_MP3_Donations.organization_id = %(organization_id)s"
        args["organization_id"] = organization_id
    
    # TODO search-8 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    #Bhavya Shah 19 November, 2023
    if column and order:
        if column in allowed_columns and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"

    # TODO search-9 append limit (default 10) or limit greater than 1 and less than or equal to 100
    #Bhavya Shah 19 November, 2023
    # TODO search-10 provide a proper error message if limit isn't a number or if it's out of bounds
    #Bhavya Shah 19 November, 2023
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

    print("query",query)
    print("args", args)
    # Check if there are errors before executing the query
    if not has_error:
        try:
            # Execute the query with the provided arguments
            result = DB.selectAll(query, args)
            if result.status:
                rows = result.rows
            else:
                # TODO search-11 make this user-friendly
                # Bhavya Shah - bs635 - 19 November, 2023
                flash("An error occurred while executing the search query. Please try again.", "danger")
        except Exception as e:
            # TODO search-12 make this user-friendly
            # Bhavya Shah - bs635 - 19 November, 2023
            print(f"search error {e}")
            flash("An error occurred while executing the search query. Please try again later.", "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    
    # TODO search-12 if request args has organization identifier set organization_name variable to the correct name
    if organization_id:
        try:
            # Fetch organization name based on organization_id
            result = DB.selectOne("SELECT name FROM IS601_MP3_Organizations WHERE id = %s", organization_id)
            if result.status:
                organization_id = result.row.get("id")
                organization_name = result.row.get("name")
            else:
                # TODO search-13 make this user-friendly
                # Bhavya Shah - bs635 - 19 November, 2023
                flash("An error occurred while fetching organization name. Please try again later.", "danger")
        except Exception as e:
            # TODO search-14 make this user-friendly
            # Bhavya Shah - bs635 - 19 November, 2023
            print(f"organization name fetch error {e}")
            flash("An error occurred while fetching organization name. Please try again later.", "danger")
    else:
        organization_name = ""  

    return render_template("list_donations.html", organization_name=organization_name, rows=rows, allowed_columns=allowed_columns)


@donations.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments
        # Bhavya Shah - bs635 - 18 November,2023
        donor_firstname = request.form.get("donor_firstname")
        donor_lastname = request.form.get("donor_lastname")
        donor_email = request.form.get("donor_email")
        organization_id = request.form.get("organization_id")
        item_name = request.form.get("item_name")
        item_description = request.form.get("item_description", "")
        item_quantity = request.form.get("item_quantity")
        donation_date = request.form.get("donation_date")
        comments = request.form.get("comments", "")
        
        # TODO add-2 donor_firstname is required (flash proper error message)
        # TODO add-3 donor_lastname is required (flash proper error message)
        # TODO add-4 donor_email is required (flash proper error message)
        # TODO add-4a email must be in proper format (flash proper message)
        # TODO add-5 organization_id is required (flash proper error message)
        # TODO add-6 item_name is required (flash proper error message)
        # TODO add-7 item_description is optional
        # TODO add-8 item_quantity is required and must be more than 0 (flash proper error message)
        # TODO add-9 donation_date is required and must be within the past 30 days
        # TODO add-10 comments are optional
        # Bhavya Shah - bs635 - 18 November,2023
        has_error = False # use this to control whether or not an insert occurs
        
        if not donor_firstname:
            has_error = True
            flash("Donor first name is required", "danger")
        if not donor_lastname:
            has_error = True
            flash("Donor last name is required", "danger")

        if not donor_email:
            has_error = True
            flash("Donor email is required", "danger")
        elif not is_valid_email(donor_email):
            has_error = True
            flash("Invalid email format", "danger")
        if not organization_id:
            has_error = True
            flash("Organization is required", "danger")
        if not item_name:
            has_error = True
            flash("Item name is required", "danger")
        if not item_quantity or not item_quantity.isdigit() or int(item_quantity) <= 0:
            has_error = True
            flash("Item quantity must be a positive integer", "danger")
        if not donation_date:
            has_error = True
            flash("Donation date is required", "danger")
        else:
            try:
                donation_date = datetime.strptime(donation_date, "%Y-%m-%d")
                if (datetime.now() - donation_date).days > 30:
                    has_error = True
                    flash("Donation date must be within the past 30 days", "danger")
            except ValueError:
                has_error = True
                flash("Invalid date format. Please use YYYY-MM-DD", "danger")
        
        if not has_error:
            try:
                result = DB.insertOne("""
                    INSERT INTO IS601_MP3_Donations (donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments)
                    VALUES (%(donor_firstname)s, %(donor_lastname)s, %(donor_email)s, %(organization_id)s, %(item_name)s, 
                            %(item_description)s, %(item_quantity)s, %(donation_date)s, %(comments)s)
                """, {
                    "donor_firstname": donor_firstname,
                    "donor_lastname": donor_lastname,
                    "donor_email": donor_email,
                    "organization_id": organization_id,
                    "item_name": item_name,
                    "item_description": item_description,
                    "item_quantity": item_quantity,
                    "donation_date": donation_date,
                    "comments": comments
                }) # <-- TODO add-11 add query and add arguments
                # Bhavya Shah - bs635 - 18 November,2023
                if result.status:
                    print("donation record created")
                    flash("Created Donation Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                # Bhavya Shah - bs635 - 18 November,2023
                print(f"insert error {e}")
                flash("There was an error creating the donation record. Please try again.", "danger")
    return render_template("manage_donation.html",donation=request.form)

@donations.route("/edit", methods=["GET", "POST"])
def edit():
    row = {}
    
    # TODO edit-1 request args id is required (flash proper error message)
    # Bhavya Shah - bs635 - 18 November,2023
    donation_id = request.args.get("id")
    if not donation_id:
        flash("Donation ID is required", "danger")
        return redirect(url_for("donations.search"))
    else:
        if request.method == "POST":
            
            # Bhavya Shah - bs635 - 18 November,2023
            # TODO add-2 retrieve form data for donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments
            donor_firstname = request.form.get("donor_firstname")
            donor_lastname = request.form.get("donor_lastname")
            donor_email = request.form.get("donor_email")
            organization_id = request.form.get("organization_id")
            item_name = request.form.get("item_name")
            item_description = request.form.get("item_description", "")
            item_quantity = request.form.get("item_quantity")
            donation_date = request.form.get("donation_date")
            comments = request.form.get("comments", "")
            
            print(donor_lastname)
            
            # TODO add-3 donor_firstname is required (flash proper error message)
            # Bhavya Shah - bs635 - 18 November,2023
            if not donor_firstname:
                flash("Donor First Name is required", "danger")
                has_error = True
            
            # TODO add-4 donor_lastname is required (flash proper error message)
            # Bhavya Shah - bs635 - 18 November,2023
            if not donor_lastname:
                flash("Donor Last Name is required", "danger")
                has_error = True
            
            # TODO add-5 donor_email is required (flash proper error message)
            # Bhavya Shah - bs635 - 18 November,2023
            if not donor_email:
                flash("Donor Email is required", "danger")
                has_error = True
            # TODO add-5a email must be in proper format (flash proper message)
            # Bhavya Shah - bs635 - 18 November,2023
            elif not is_valid_email(donor_email):  # You need to implement validate_email function
                flash("Email must be in a proper format", "danger")
                has_error = True
            
            # TODO add-6 organization_id is required (flash proper error message)
            # Bhavya Shah - bs635 - 18 November,2023
            if not organization_id:
                flash("Organization ID is required", "danger")
                has_error = True
            
            # TODO add-7 item_name is required (flash proper error message)
            # Bhavya Shah - bs635 - 18 November,2023
            if not item_name:
                flash("Item Name is required", "danger")
                has_error = True
            
            # TODO add-8 item_description is optional
            
            # TODO add-9 item_quantity is required and must be more than 0 (flash proper error message)
            # Bhavya Shah - bs635 - 18 November,2023
            if not item_quantity or int(item_quantity) <= 0:
                flash("Item Quantity must be greater than 0", "danger")
                has_error = True
            
            # TODO add-10 donation_date is required and must be within the past 30 days
            # Bhavya Shah - bs635 - 18 November,2023
            # You can use a datetime library for this check
            try:
                donation_date = datetime.strptime(donation_date, "%Y-%m-%d")
                thirty_days_ago = datetime.now() - timedelta(days=30)
                if donation_date < thirty_days_ago:
                    flash("Donation Date must be within the past 30 days", "danger")
                    has_error = True
            except ValueError:
                flash("Invalid Date Format", "danger")
                has_error = True
            
            # TODO add-11 comments are optional
            
            has_error = False  # use this to control whether or not an insert occurs
                
            if not has_error:
                try:
                    # TODO edit-12 fill in proper update query
                    # Bhavya Shah - bs635 - 18 November,2023
                    result = DB.update("""
                    UPDATE IS601_MP3_Donations SET
                    donor_firstname = %s,
                    donor_lastname = %s,
                    donor_email = %s,
                    organization_id = %s,
                    item_name = %s,
                    item_description = %s,
                    item_quantity = %s,
                    donation_date = %s,
                    comments = %s
                    WHERE id = %s
                    """, donor_firstname, donor_lastname, donor_email, organization_id, item_name,
                        item_description, item_quantity, donation_date, comments, donation_id,)
                    
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-13 make this user-friendly
                    # Bhavya Shah - bs635 - 18 November,2023
                    
                    print(f"update error {e}")
                    flash("An error occurred while updating the record. Please try again later.", "danger")
        
        try:
            # TODO edit-14 fetch the updated data 
            # Bhavya Shah - bs635 - 18 November,2023
            result = DB.selectOne("""SELECT 
            IS601_MP3_Donations.id, donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments
            FROM IS601_MP3_Donations LEFT JOIN IS601_MP3_Organizations ON IS601_MP3_Donations.organization_id = IS601_MP3_Organizations.id
            WHERE IS601_MP3_Donations.id = %s
            """, donation_id)
            
            if result.status:
                row = result.row
                #print(row)
        except Exception as e:
            # TODO edit-15 make this user-friendly
            # Bhavya Shah - bs635 - 18 November,2023
            flash("An error occurred while fetching the updated data. Please try again later.", "danger")

    return render_template("manage_donation.html", donation=row)


@donations.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 if id is missing, flash necessary message and redirect to search
    # Bhavya Shah - bs635 - 18 November,2023
    donation_id = request.args.get("id")
    if not donation_id:
        flash("Donation ID is required", "danger")
        return redirect(url_for("donations.search"))

    # TODO delete-2 delete donation by id (fetch the id from the request)
    # Bhavya Shah - bs635 - 18 November,2023
    try:
        result = DB.delete("DELETE FROM IS601_MP3_Donations WHERE id = %s", donation_id)
        if result.status:
            # TODO delete-3 ensure a flash message shows for successful delete
            # Bhavya Shah - bs635 - 18 November,2023
            flash("Deleted record", "success")
        else:
            # TODO delete-4 handle error case and show flash message
            # Bhavya Shah - bs635 - 18 November,2023
            flash("An error occurred while deleting the record. Please try again.", "danger")
    except Exception as e:
        # TODO delete-4 handle error case and show flash message
        # Bhavya Shah - bs635 - 18 November,2023
        flash(f"Delete error: {e}", "danger")

    # TODO delete-5 redirect to donation search
    # Bhavya Shah - bs635 - 18 November,2023
    return redirect(url_for("donations.search"))