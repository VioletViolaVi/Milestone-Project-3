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
            "booked_by": session["user"].title()
        }
        mongo.db.booked_details.insert_one(bookings)
        flash("Booking Successfully Added!")
        return redirect(url_for("my_bookings"))

    # movie info taken from mongo db for dropdown
    movie_names = list(mongo.db.movies.find())
    # location info taken from mongo db for dropdown
    location_names = list(mongo.db.locations.find().sort("location_name", 1))
    # reviews brought out from mongo db for homepage
    reviews = list(mongo.db.reviews.find())

    return render_template("index.html", page_title="Our Movies",
                           page_subtitle="Reviews",
                           page_title2="About Us",
                           movie_names=movie_names,
                           location_names=location_names,
                           reviews=reviews)


@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        # searches for same username in mongo db for comprison
        existing_username = mongo.db.users.find_one(
            {"user": request.form.get("username").lower()})

        # searches for same email in mongo db for comprison
        existing_user_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        # occurs when username or email typed is same as that in db
        if existing_username or existing_user_email:
            flash("Username And/Or Email Already Registered!")
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
        flash(f"Welcome {request.form.get('username').capitalize()}!")
        return redirect(url_for("home"))

    return render_template("signup.html", page_title="Sign Up")


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
                flash(
                    f"Welcome Back {request.form.get('username').capitalize()}!")
                return redirect(url_for("home"))
            else:
                # occurs when password is wrong
                flash("Incorrect Username And/Or Password")
                return redirect(url_for("login"))
        else:
            # occurs when not an existing user
            flash("Incorrect Username And/Or Password")
            return redirect(url_for("login"))

    return render_template("login.html", page_title="Log In")


@app.route("/my_bookings", methods=["GET", "POST"])
def my_bookings():

    # reviews left by users
    if request.method == "POST":

        reviews = {
            "reviewed_movie_name": request.form.get("selectedMovie"),
            "user_review": request.form.get("commentBox"),
            "user": session["user"].title()
        }

        mongo.db.reviews.insert_one(reviews)
        flash("Review Successfully Posted!")
        return redirect(url_for("home"))

    # movie info taken from mongo db for dropdown
    movie_names = list(mongo.db.movies.find().sort("movie_name", 1))
    # location info taken from mongo db for dropdown
    location_names = list(mongo.db.locations.find().sort("location_name", 1))
    # booking info brought out from mongo db
    booking_info = mongo.db.booked_details.find()

    return render_template("my_bookings.html", page_title="My Bookings",
                           movie_names=movie_names,
                           location_names=location_names,
                           booking_info=booking_info)


@app.route("/change_booking/<booked_details_id>", methods=["GET", "POST"])
def change_booking(booked_details_id):

    # changing booked details from db
    mongo.db.booked_details.update(
        {"_id": ObjectId(booked_details_id)},
        {
            "booked_movie": request.form.get("bookedMovie"),
            "booked_ticket_quantity": request.form.get("ticketQuantity"),
            "booked_date": request.form.get("date"),
            "booked_location": request.form.get("location"),
            "booked_by": session["user"].title()
        })

    flash("Booking Successfully Updated!")
    return redirect(url_for("my_bookings"))


@app.route("/delete_booking/<booked_details_id>")
def delete_booking(booked_details_id):

    # targets bookings in db by their _id
    mongo.db.booked_details.remove({"_id": ObjectId(booked_details_id)})
    flash("Booking Successfully Deleted!")
    return redirect(url_for("my_bookings"))


@app.route("/admin")
def admin():

    # booking info brought out from mongo db
    booking_info = mongo.db.booked_details.find().sort("booked_by", 1)
    # location info taken from mongo db for dropdown
    location_names = list(
        mongo.db.locations.find().sort("location_name", 1))
    # movie info taken from mongo db for dropdown
    movie_names = list(mongo.db.movies.find().sort("movie_name", 1))
    # reviews brought out from mongo db for admin
    reviews = list(mongo.db.reviews.find().sort("user", 1))
    # users brought out from mongo db for admin
    users = list(mongo.db.users.find().sort("user", 1))

    return render_template("admin.html", page_title="Administration",
                           bookings_title="User Bookings",
                           locations_title="Cinemagic Locations",
                           movies_title="Cinemagic Movies",
                           users_reviews_title="User Reviews",
                           users_title="Cinemagaic Users",
                           booking_info=booking_info,
                           location_names=location_names,
                           movie_names=movie_names,
                           reviews=reviews,
                           users=users)


@app.route("/admin_add_movie", methods=["GET", "POST"])
def admin_add_movie():

    # add movies
    if request.method == "POST":

        added_movie = {
            "movie_name": request.form.get("addMovieName"),
            "rating": request.form.get("addMovieRating"),
            "duration": request.form.get("addMovieDuration"),
            "genres": request.form.get("addMovieGenre"),
            "synopsis": request.form.get("addMovieSynopsis"),
            "director": request.form.get("addMovieDirector"),
            "writer": request.form.get("addMovieWriter"),
            "producer": request.form.get("addMovieProducer"),
            "cast": request.form.get("addMovieCast")
        }

        mongo.db.movies.insert_one(added_movie)
        flash("New Movie Successfully Added!")
        return redirect(url_for("admin"))


@app.route("/admin_change_movie/<movie_id>", methods=["GET", "POST"])
def admin_change_movie(movie_id):

    # changing movies from db
    mongo.db.movies.update(
        {"_id": ObjectId(movie_id)},
        {
            "movie_name": request.form.get("changeMovieName"),
            "movie_poster": request.form.get("changeMoviePoster"),
            "rating": request.form.get("changeMovieRating"),
            "duration": request.form.get("changeMovieDuration"),
            "genres": request.form.get("changeMovieGenre"),
            "synopsis": request.form.get("changeMovieSynopsis"),
            "director": request.form.get("changeMovieDirector"),
            "writer": request.form.get("changeMovieWriter"),
            "producer": request.form.get("changeMovieProducer"),
            "cast": request.form.get("changeMovieCast")
        })

    flash("Movie Successfully Updated!")
    return redirect(url_for("admin"))


@app.route("/admin_delete_movie/<movie_id>")
def admin_delete_movie(movie_id):

    # targets movies in db by their _id
    mongo.db.movies.remove({"_id": ObjectId(movie_id)})
    flash("Moive Successfully Deleted!")
    return redirect(url_for("admin"))


@app.route("/admin_add_location", methods=["GET", "POST"])
def admin_add_location():

    # add locations
    if request.method == "POST":

        added_location = {
            "location_name": request.form.get("addingLocations")
        }

        mongo.db.locations.insert_one(added_location)
        flash("New Location Successfully Added!")
        return redirect(url_for("admin"))


@app.route("/admin_change_location/<location_name_id>",
           methods=["GET", "POST"])
def admin_change_location(location_name_id):

    # changing movies from db
    mongo.db.locations.update(
        {"_id": ObjectId(location_name_id)},
        {
            "location_name": request.form.get("changeLocation")
        })

    flash("Location Successfully Updated!")
    return redirect(url_for("admin"))


@app.route("/admin_delete_location/<location_name_id>")
def admin_delete_location(location_name_id):

    # targets locations in db by their _id
    mongo.db.locations.remove({"_id": ObjectId(location_name_id)})
    flash("Location Successfully Deleted!")
    return redirect(url_for("admin"))


@app.route("/logout")
def logout():

    flash("You Have Been Logged Out!")
    # removes session cookies to logout
    session.pop("user")
    return redirect(url_for("home"))


# DELETE LATER!!! SET DEBUG TO FALSE!!!!
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(
        os.environ.get("PORT")), debug=True)
