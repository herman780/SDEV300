# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 22:00:38 2022
Lab 6: Generation of simple website using Python Flask
@author: Herman Mann
"""
#This application will focus on the different countries I would
#like to visit and for what reason. Total of 4 routes (4 webpages)
#index.html, France.html, Spain.html, and Germany.html
from datetime import datetime
from flask import Flask
from flask import render_template
#Needed for opening and running the Flask program execution.
app = Flask(__name__)
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
def home_page():
    """ This function is designed as the root page for all
    webpages and will post the current date and time on the
    webpage """
    date_today = get_current_time_and_date()
    return render_template('index.html', content=[date_today])
#This is the second route (second webpage) which is the France.html
@app.route('/France')
def france():
    """ This will be used for the Paris Webpage """
    return render_template('France.html')
#This is the third route (third webpage) which is the Spain.html
@app.route('/Spain')
def spain():
    """ This will be used for the Spain Webpage """
    return render_template('Spain.html')
#This is the fourth route (fourth webpage) which is the Germany.html
@app.route('/Germany')
def germany():
    """ This will be used for the Germany Webpage """
    return render_template('Germany.html')
#Starts the executing of program once program enters main.
if __name__ == "__main__":
    app.run(debug=True)
