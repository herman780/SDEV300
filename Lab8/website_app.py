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
import os
from os.path import exists
from datetime import datetime
from string import punctuation
from flask import Flask, flash, render_template, abort, session, request, redirect, url_for
from passlib.hash import sha256_crypt

NEW_PASS_FILE = "newpassfile"
COMMON_PASSWORDS_USED = "CommonPassword.txt"

#This is a temporary file to store passwords entered
#Only hashed versions of the passwords are stored here
#not the original passwords itself
TEMP_PASS_FILE = "temppassfile"

#This is the direct location of where to locate
#failed logins by user attempts.
USER_FAILED_LOGINS = "user_failed_logins"

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

#Adding the user entered password to the commonly used password list
#Commonpassword.txt so the same password is not used again
typical_common_passwords = set()
with open(COMMON_PASSWORDS_USED, "r") as typical_common_passwords_file:
    for entered_password_session in typical_common_passwords:
        typical_common_passwords.add(entered_password_session.strip())
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
def right_user_match(curr_username, curr_password):
    """ This function checks to see if the username and password
    of associated user is valid. Returns True if it is valid, False
    if not. """
    with open(NEW_PASS_FILE, "r") as newpassfile:
        for stored_pass_information in newpassfile:
            try:
                username_valid = False
                password_valid = False
                r_username, r_salt_hash = stored_pass_information.split()
                if curr_username == r_username:
                    username_valid = True
                if sha256_crypt.verify(curr_password, r_salt_hash):
                    password_valid = True
                if username_valid and password_valid:
                    return True
            except ValueError:
                pass
    return False
#This function is designed to check and see if the new password matches,
#and also if the new password is complex enough, and also if the new password
#is commonly found in frequently used passwords.
def check_new_pass_match(pass1, pass2):
    """ This function performs password tests to test and see if
    the new passwords entered match each other or not """
    not_match_error = False
    if not pass1 == pass2:
        not_match_error = "The new passwords do not match"
    elif pass1 in typical_common_passwords:
        not_match_error = "The new password is commonly used. Please use another password."
    elif not check_password_complex(pass1):
        not_match_error = "The new password is not complex enough. Try to make it more complex."
    
    return not_match_error
def logger_check_test(curr_username):
    """ This function is designed to create a log that logs all failed login
    attempts. The log will include the date, time, and the IP address. Logs the
    failed login attempts to a specific file. """
    
    if not exists(USER_FAILED_LOGINS):
        open(USER_FAILED_LOGINS, "w").close()
            
    current_time = datetime.now()
    
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        retrieve_Ip_address = request.environ['REMOTE_ADDR']
    else:
        retrieve_Ip_address = request.environ['HTTP_X_FORWARDED_FOR'] # if behind a proxy
        
    with open(USER_FAILED_LOGINS, "a") as logfile:
        logfile.write(current_time.isoformat() + " " + retrieve_Ip_address + " " 
                              + curr_username + "\n")
    
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
        username = request.form["username"]
        password = request.form["password"]
        
        #recording failed logins here for the current user
        if not right_user_match(username, password):
            flash("Invalid username or password entered.")
            logger_check_test(username)
        # else the current user will have access to the main index page
        else:
            session["username"] = username
            return redirect(url_for("index"))
        
    else:
        if "username" in session:
            return redirect(url_for("index"))
    #returning the rendered login.html template for the login form
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
#This route resembles the Password update form, and the accompanied content
#follows for the Password update form information.
@app.route('/change_update_password', methods=["POST", "GET"])
def change_update_password():
    """ This function is designed for the change_update_password form webpage """
    if request.method == "POST":
        encounter_error = None
        if "username" in session:
            curr_username = session["username"]
            prev_password = request.form["Old Password"]
            new_pass1 = request.form["New Password"]
            new_pass2 = request.form["Re-enter New Password"]
           
            encounter_error = check_new_pass_match(new_pass1, new_pass2)
           
            if not right_user_match(curr_username, prev_password):
                encounter_error = "Incorrect old password entered"
            #if error is produced the message will be displayed on the change password form.
            if encounter_error:
                flash(encounter_error)
               
            else:
                with open(NEW_PASS_FILE, "r") as newpassfile:
                    with open(TEMP_PASS_FILE, "a") as temppassfile:
                        for stored_pass_information in newpassfile:
                            try:
                                r_username, r_salt_hash = stored_pass_information.split()
                                identical_username = curr_username == r_username
                                identical_password = sha256_crypt.verify(prev_password, r_salt_hash)
                                if identical_username and identical_password:
                                    t_salt_hash = sha256_crypt.hash(new_pass1)
                                    temppassfile.write(curr_username + " " + t_salt_hash + "\n")
                                else:
                                    temppassfile.write(r_username + " " + r_salt_hash + "\n")
                            except ValueError:
                                pass
                  # used for removing the password backup file that could potentially
                  # have been previously created
                try:
                    os.remove(NEW_PASS_FILE + ".bak")
                except OSError:
                    pass
               
                # Making sure there is a backup file saved of the previous newpassfile
                os.rename(NEW_PASS_FILE, NEW_PASS_FILE + ".bak")
                os.rename(TEMP_PASS_FILE, NEW_PASS_FILE)
                flash("Password has been Updated")
                return render_template("index.html")
        else:
            flash("You must be logged in to change password.")
            return redirect(url_for("login"))
    # returning the final change password form template and rendering it
    return render_template("change_update_password.html")
           
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
