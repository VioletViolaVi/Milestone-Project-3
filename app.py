import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    # books tickets
    if request.method == "POST":
        bookings = {
            "booked_movie": request.form.get("bookedMovie"),
            "booked_ticket_quantity": request.form.get("ticketQuantity"),
            "booked_date": request.form.get("date"),
            "booked_location": request.form.get("location"),
            "booked_by": session["user"]
        }
        mongo.db.booked_details.insert_one(bookings)
        flash("Booking Successfully Added!")
        return redirect(url_for("my_bookings"))

    # movie info taken from mongo db for dropdown
    movie_names = list(mongo.db.movies.find())
    # location info taken from mongo db for dropdown
    location_names = list(mongo.db.locations.find())
    # booking info taken from mongo db
    booking_info = mongo.db.booked_details.find()
    # review info taken from mongo db
    reviews = mongo.db.reviews.find()

    return render_template("index.html", movie_names=movie_names,
                           location_names=location_names,
                           booking_info=booking_info, reviews=reviews)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # searches for same username in mongo db for comprison
        existing_user = mongo.db.users.find_one(
            {"user": request.form.get("username").lower()})

        # occurs when username typed is same as username found by above code
        if existing_user:
            flash("Username Already Exists!")
            # takes users back to signup page to try signing up again
            return redirect(url_for("signup"))

        # (else) saves signup form input when usernames are not matched
        signup = {
            "user": request.form.get("username").lower(),
            "email":  request.form.get("email").lower(),
            "pwd": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(signup)

        # puts new user in session cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign Up Successful!")
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checks if username exists in db
        existing_user = mongo.db.users.find_one(
            {"user": request.form.get("username").lower()})

        if existing_user:
            # checks if hashed password matches input
            if check_password_hash(
                    existing_user["pwd"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash(f"Welcome back {request.form.get('username')}!")
                return redirect(url_for("home"))
            else:
                # occurs when password is wrong
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # occurs when not an existing user
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/my_bookings")
def my_bookings():
    # books tickets and saves in mongo db
    if request.method == "POST":
        bookings = {
            "booked_movie": request.form.get("bookedMovie"),
            "booked_ticket_quantity": request.form.get("ticketQuantity"),
            "booked_date": request.form.get("date"),
            "booked_location": request.form.get("location"),
            "booked_by": session["user"]
        }
        mongo.db.booked_details.insert_one(bookings)
        flash("Booking Successfully Added!")
        return redirect(url_for("my_bookings"))

    # booking info taken from mongo db
    booking_info = mongo.db.booked_details.find()

    movie_names = list(mongo.db.movies.find())
    location_names = list(mongo.db.locations.find())

    return render_template("my_bookings.html", movie_names=movie_names,
                           location_names=location_names,
                           booking_info=booking_info)


@app.route("/logout")
def logout():
    flash("You have been logged out!")
    # removes session cookies to logout
    session.pop("user")
    return redirect(url_for("home"))


# if request.method == "POST":
#     provided_review = {
#         "user": request.form.get("username").lower(),
#         "movie_name": request.form.get("selectedMovie").lower(),
#         "star_rating": request.form.get("starRating").lower(),
#         "user_review": request.form.get("commentBox").lower()
#     }


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(
        os.environ.get("PORT")), debug=True)
