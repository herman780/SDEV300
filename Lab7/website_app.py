# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 22:00:38 2022
Lab 6: Generation of simple website using Python Flask
@author: Herman Mann
"""
#This application will focus on the different countries I would
#like to visit and for what reason. Total of 4 routes (7 webpages)
#login.html, registration.html, index.html, France.html,
#Spain.html, Germany.html, and table.html
from os.path import exists
from datetime import datetime
from string import punctuation
from flask import Flask, flash, render_template, abort, session, request, redirect, url_for
from passlib.hash import sha256_crypt

NEW_PASS_FILE = "newpassfile"

#Needed for opening and running the Flask program execution.
app = Flask(__name__)
app.debug = True
#using any secret key for hashing to make sure registration or login information
#is not identical
app.secret_key = 'authenticatedsecretkey'

#Opening a new file and writing to it for storing usernames and passwords
if not exists(NEW_PASS_FILE):
    with open(NEW_PASS_FILE, "w") as file:
        file.close()
def if_user_registered(curr_sess_username):
    """ This function checks to make sure the certain user already registered
    in the overall new_pass_file """
    #checking to see if user is already registered by using salt hashing strategy
    with open(NEW_PASS_FILE, "r") as newpassfile:
        for name_already_registered in newpassfile:
            r_username, r_salt_hash = name_already_registered.split()
            r_salt_hash = r_salt_hash + "blank"
            if curr_sess_username == r_username:
                return True
    return False

def checking_for_whitespace(user_string):
    """ This function is designed to check to make sure
    if a string contains spaces or not. For example if the username entered by
    the person contains spaces this function will return that and will implicitly
    say that string contains the spaces """
    #this string will be used as a test string to test if string contains any whitespace
    #characters or not
    entered_string = user_string.split()
    #returns the length of the string given if the string contains whitespace (i.e. username)
    return len(entered_string) > 1

def check_password_complex(user_password):
    """ This function is designed to check the password complexity requirements
    of a password entered by a user.
    The complexity requirements are as follows:
        -Password must be at least 12 characters in length
        -Password must include at least 1 uppercase character
        -Password must include at least 1 lowercase character
        -Password must include at least 1 number
        AND
        -Password must include at least 1 special character.
    """
    #Checking the user entered password complexity
    if len(user_password) >= 12:
        if any(the_character.islower() for the_character in user_password):
            if any(the_character.isupper() for the_character in user_password):
                if any(the_character.isdigit() for the_character in user_password):
                    if any(the_character in punctuation for the_character in user_password):
                        return True
    #return False if password does not meet one of the required password complexities
    return False
#This function is designed to get the current date and time
#and then display it on the webpage.
#returns the current date and time in the appropriate format.
def get_current_time_and_date():
    """ Returns the current time and date """
    time_today = datetime.now()
    date_today = time_today.strftime("%B %d %Y, %I:%M:%S %p")
    return date_today
#The first page which is the root page for all of the other webpages.
#This sets the stone for all of the other webpages to lean on when
#developing their own routes. This is the index.html webpage
@app.route('/')
def index():
    """ This function is designed as the root page for all
    webpages and will post the current date and time on the
    webpage """
    date_today = get_current_time_and_date()
    if "username" in session:
        return render_template("index.html", content=[date_today])
    return redirect(url_for("login"))
#This is the app route used for developing the overall login form, so the user
#can have the ability to login.
@app.route('/login', methods=["POST", "GET"])
def login():
    """ This function will be used for designing the login html webpage,
    so the user can have access to the entirety of the website. """
    if request.method == "POST":
        curr_sess_username = request.form["username"]
        curr_sess_password = request.form["password"]
        #setting and initializing the needed variables for the login form
        authenticate_user = False
        authenticate_user_pass = False
        #checking to see if user is already logged in using the salt hashing strategy
        with open(NEW_PASS_FILE, "r") as newpassfile:
            for name_already_registered in newpassfile:
                r_username, r_salt_hash = name_already_registered.split()
                if curr_sess_username == r_username:
                    authenticate_user = True
                    #this test will verify if the entered password matches with any
                    #passwords that have been stored before or entered before
                    #if they don't match user may proceed further, else user won't
                    #breaks statement to allow user to progress further
                    if sha256_crypt.verify(curr_sess_password, r_salt_hash):
                        authenticate_user_pass = True
                        break
                authenticate_user = False
                authenticate_user_pass = False
        # if the correct associated username or password is not entered
        # a flash message will be displayed.
        if not authenticate_user or not authenticate_user_pass:
            flash("Invalid username or password entered")
        # else the username that was entered will be stored and will take the user
        # to the index webpage
        else:
            session["username"] = curr_sess_username
            return redirect(url_for("index"))
    else:
        if "username" in session:
            return redirect(url_for("index"))
    #The login.html webpage form will be successfully rendered for the user
    #to login and access the content presented on other webpages
    return render_template("login.html")
@app.route("/logout")
def logout():
    """ Serves the logout webpage """
    if "username" in session:
        session.pop("username", None)
        flash("You have successfully logged out.")
    return redirect(url_for("index"))
#This is for the registration form and to have access to it for a new user
#to register
@app.route("/registration", methods=["POST", "GET"])
def registration():
    """ Serving the Registration.html webpage for user to sign up in case
    if they are not logged in or do not have access """
    if request.method == "POST":
        if "username" in session:
            flash("Logout to create a new registration.")
        #Initializing new variables to be used for the creation of the
        #registration form
        curr_sess_username = None
        curr_sess_password = None
        error_status = None
        curr_sess_username = request.form["username"]
        curr_sess_password = request.form["password"]
        #The following are messages that could potentially be displayed for either
        #not entering a username, not entering a password, if the username is
        #already registered, if the username contains more than one space, or
        #the password that was entered does not meet all of the password complexity
        #requirements
        if not curr_sess_username:
            error_status = "Please enter a Username"
        elif not curr_sess_password:
            error_status = "Please enter a Password."
        elif if_user_registered(curr_sess_username):
            error_status = "Username already registered."
        elif checking_for_whitespace(curr_sess_username):
            error_status = "Username must not contain any spaces"
        elif not check_password_complex(curr_sess_password):
            error_status = "The entered password is not complex enough."
        #Using flash messaging to display the appropriate message based on the
        #above conditional statements
        if error_status:
            flash(error_status)
        else:
            password_hash_tech = sha256_crypt.hash(curr_sess_password)
            with open(NEW_PASS_FILE, "a") as newpassfile:
                newpassfile.write(curr_sess_username + " " + password_hash_tech + "\n")
            flash("Registration successful. Please login.")
            return redirect(url_for("login"))
    #Successfully allowing the user to register by rendering the finalized
    #registration form
    return render_template("registration.html")
#This authenticates a new user with their name on it
@app.route('/user')
def user():
    """ Serving the page of user's name on it. """
    if "username" in session:
        username = session["username"]
        return f"<h1>{username}</h1>"
    return redirect(url_for("login"))
#This is the second route (second webpage) which is the France.html
@app.route('/France')
def france():
    """ This will be used for the Paris Webpage """
    if "username" in session:
        return render_template('France.html')
    return abort(401)
#This is the third route (third webpage) which is the Spain.html
@app.route('/Spain')
def spain():
    """ This will be used for the Spain Webpage """
    if "username" in session:
        return render_template('Spain.html')
    return abort(401)
#This is the fourth route (fourth webpage) which is the Germany.html
@app.route('/Germany')
def germany():
    """ This will be used for the Germany Webpage """
    if "username" in session:
        return render_template('Germany.html')
    return abort(401)
@app.route('/table')
def table():
    """Serves a table of the current NBA Playoffs 2021-2022 picture
    along with that the famous NBA athletes, and past famous NBA teams who made
    the playoffs in the past"""
    if "username" in session:
        return render_template("table.html")
    return abort(401)
#Starts the executing of program once program enters main.
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
