# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:25:12 2022

@author: Herman Mann
"""
from decimal import Decimal
import string
import secrets
#import date
import math
from datetime import date
SELECTION_CHOICES = {'a', 'b', 'c', 'd', 'e', 'f'}
SELECTION_YES = {'YES','Yes', 'y', 'Y'}
SELECTION_OPTIONS_NO = {'NO','No', 'n', 'N'}

#Start of the  command line menu-driven python application
print('Hello user, welcome to the command line menu')

#Displaying the menu of options for the user to select from
def displaying_menu():
    """ Displaying the menu options the user has options from selecting """
    #The menu option for generating a secure password.
    print('a. Generate Secure Password')
    #The menu option to calculate and Format a percentage entered by user.
    print('b. Calculate and Format a Percentage')
    #The menu option which produces the total days until July 4, 2025.
    print('c. How many days from today until July 4, 2025?')
    #The menu option to calculate the leg of a triangle.
    print('d. Use the law of Cosines to calculate the leg of a triangle.')
    #The menu option to calculate the volume of a right cylinder
    #given the radius and height by the user.
    print('e. Calculate the volume of a Right Circular Cylinder')
    #The menu option to exit and terminate the program.
    print('f. Exit program')
def user_entering_option():
    """ This is a function to display the different menu options
    that are supposed to be presented from the user to pick from """
    user_selection_choice = None
    while user_selection_choice not in SELECTION_CHOICES:
        #User will enter a choice between a and f through here.
        user_selection_choice = input('Enter a Choice (a-f): ').lower()
        #returning the user's menu selection choice.
    return user_selection_choice

def getting_yes_or_no(message):
    """ This is a function to return a user input of either Yes or
    No based on the menu option selected by the user """
    user_input = None
    while not user_input:
        user_input = input(message).upper()
        #If user does not enter yes or no, user_input would not
        #work accordingly.
        if user_input not in SELECTION_YES and user_input not in SELECTION_OPTIONS_NO:
            user_input = None
    #returning the user input, which is either a yes or no depending
    #on which menu option selected.
    return user_input

def securing_password():
    """ This function is designed to generate a secure password,
    per user choosing and depends on the different complexities the
    user wants for the password, the more complexity the more secure
    the password is """
    the_length_of_password = None
    if_lowercase = None
    if_uppercase = None
    if_digit = None
    if_special_character = None
    #User will input the total length of their password
    while not the_length_of_password:
        the_length_of_password = (input("length of the password, and it must be positive: "))
        if not the_length_of_password.isdigit():
            the_length_of_password = None
        if int(the_length_of_password) <= 0:
            the_length_of_password = None
    #storing the result of the length of password as an integer amount
    the_length_of_password = int(the_length_of_password)
    #The different complexities will be used for the password here
    while not (if_lowercase or if_uppercase or if_digit or if_special_character):
        #If the user chooses to use lowercase characters for the password
        #here would be the place it will run through
        if_lowercase = getting_yes_or_no('lowercase letters (y or n): ') in SELECTION_YES
        #If the user chooses to use uppercase characters for the password
        #here would be the place it will run through
        if_uppercase = getting_yes_or_no('Uppercase letters (y or n): ') in SELECTION_YES
        #If the user chooses to use numbers for the password, the user
        #may choose to do so starting from the process here.
        if_digit = getting_yes_or_no('Contain digits (y or n): ') in SELECTION_YES
        #If user chooses to use special characters for the password
        #the user may choose to do so, processing will begin here.
        if_special_character = getting_yes_or_no('Special characters (y or n): ') in SELECTION_YES
        #If user chooses to not use any complexities, a message would be
        #printed to make sure the user uses at least one complexity type
        #to make the password more secure than not to do so making it
        #less secure
        if not(if_lowercase or if_uppercase or if_digit or if_special_character):
            print('The password must contain complexity (Either lowercase, uppercase, numbers ' +
                  'special characters).')
    #returning the different complexities that will be used for
    #making the secure password for the user.
    return the_length_of_password, if_lowercase, if_uppercase, if_digit, if_special_character
def sending_params_secure_password(arguments):
    """ This function is designed for the user to enter the parameters
    per there designation for the different complexity types of password """
    the_length_of_password, if_lowercase, if_uppercase, if_digit, if_special_character = arguments
    password_entered = ''
    #if user chooses to have lowercase complexity, this will be added
    #on to the user's password entered previously
    if if_lowercase:
        password_entered = password_entered + string.ascii_lowercase
    #if the user chooses to have uppercase complexity, this will be added
    #to the password the user entered previously
    if if_uppercase:
        password_entered = password_entered + string.ascii_uppercase
    #if the user chooses to have numbers complexity, this will be added
    #to the password the user entered previously
    if if_digit:
        password_entered = password_entered + string.digits
    #if user chooses to use special characters complexity, this will
    #be added to the password the user entered previously
    if if_special_character:
        password_entered = password_entered + string.punctuation
    #returning the added complexities onto the password entered by user
    #depending how long the password length is
    return ''.join(secrets.choice(password_entered) for i in range(the_length_of_password))
def calculate_and_format_percentage():
    """ This function is designed for implementing the second menu
    option, which has the user enter a numerator value, denominator value,
    and storing the amount of decimals being added after the decimal
    point, basically for formatting a number into a whole percentage """
    if_total_decimals = None
    numerator_value = None
    denominator_value = None
    #Welcome message, specifically designed for the second menu option
    print('Hello user, welcome to the calculating and formating a percentage')
    print('module. You will enter a numerator, denominator, and decimals')
    print('and how many decimal places you like to use for displaying purposes')
    print('The program will then do some calculation to display the number')
    print('and then depending on how many decimal points you would like')
    print('to have, the program will round accordingly to that amount.')
    #user will input the numerator value through here, and processing of
    #the value with the different conditions will be started
    while not numerator_value:
        numerator_value = input('Enter a value for numerator here (must be positive): ')
        if not numerator_value.isdecimal():
            numerator_value = None
    #setting the numerator value specifically chosen by the user
    numerator_value = Decimal(numerator_value)
    #user will input the denominator value through here, and processing of
    #the value with the different conditions will be started
    while not denominator_value:
        denominator_value = input('Enter a value for denominator here (must be positive): ')
        #if the denominator value entered by user is equal to 0,
        #user will be prompted to enter a valid value for denominator
        if int(denominator_value) == 0:
            denominator_value = None
        if not denominator_value.isdecimal():
            denominator_value = None
    #setting the denominator value specifically chosen by the user
    denominator_value = Decimal(denominator_value)
    #user will enter the total number of decimal points wanted
    #after formatting the numerator/denominator number as a number
    #percentage
    while not if_total_decimals:
        if_total_decimals = input('Enter the number of decimals you wish to display: ')
        if not if_total_decimals.isdecimal():
            if_total_decimals = None
        elif int(if_total_decimals) < 0:
            if_total_decimals = None
    #setting the total number of decimal points user wants for
    #the proper format of the percentage number
    if_total_decimals = int(if_total_decimals)
    #returning the numerator, denominator, and decimal points values
    #as entered and processed by user
    return numerator_value, denominator_value, if_total_decimals
def calculating_and_format_percentage(arguments):
    """ This function is specifically used for sending in the parameters
    for the accurate formating of the calculation of percentage
    of the number entered by user as supposedly being processed """
    numerator_value, denominator_value, if_total_decimals = arguments
    percentage_calculated = (numerator_value/denominator_value)
    #formatting the final percentage number
    percentage_calculated = str(round(percentage_calculated * 100, if_total_decimals)) + "%"
    #returning the percentage number depending on user entered numbers
    return percentage_calculated
def calculation_law_cosines():
    """ This function is designed to use the law of cosines to
    calculate the unknown side of the triangle which is C in this case """
    a_side = None
    b_side = None
    c_or_opposite_side = None
    #user will enter the value for side a here, being it is positive only
    while not a_side:
        a_side = input('Side A Value (must be a positive number): ')
        if not a_side.isdecimal():
            a_side = None
        if not Decimal(a_side) > 0:
            a_side = None
    #setting the a_side value as entered by user
    a_side = Decimal(a_side)
    #user will enter the value for side b here, being it is positive only
    while not b_side:
        b_side = input('Side B Value (must be a positive number): ')
        if not b_side.isdecimal():
            b_side = None
        if not Decimal(b_side) > 0:
            b_side = None
    #setting the side b value as chosen by the user
    b_side = Decimal(b_side)
    #user will enter the opposite angle value of triangle here
    while not c_or_opposite_side:
        c_or_opposite_side = input('The opposite angle Value (must be a positive number): ')
        if not c_or_opposite_side.isdecimal():
            c_or_opposite_side = None
        if not Decimal(c_or_opposite_side) > 0:
            c_or_opposite_side = None
    #setting the final value of the opposite angle side of triangle
    c_or_opposite_side = Decimal(c_or_opposite_side)
    #returning side a, side b, and the opposite side values as
    #entered by the user
    return a_side, b_side, c_or_opposite_side
def the_calculation_law_cosines(arguments):
    """ This function allows the user to enter the parameters utilizing
    the law of cosines processing function to get the final value
    of side C as served for the menu option at the start of the
    program """
    a_side, b_side, c_or_opposite_side = arguments
    degree_in_cosine = Decimal(math.cos(c_or_opposite_side))
    #the calculation of obtaining the c side of the triangle
    #dependent on the values entered by user for side a, side b,
    #and the opposite angle side
    c_squared = (a_side ** 2) + (b_side ** 2) - ((2 * a_side * b_side) * degree_in_cosine)
    #storing the calculated c side value
    c_side = c_squared.sqrt()
    #returning the c side value here
    return c_side
def calculation_right_cylinder():
    """ This function is used for calculating the volume of a
    right circular cylinder """
    the_radius = None
    the_height = None
    #user will enter the radius value here of the right circular cylinder
    while not the_radius:
        the_radius = input('Enter the radius value (must be a positive number): ')
        if not the_radius.isdecimal():
            the_radius = None
        if not Decimal(the_radius) > 0:
            the_radius = None
    #setting the radius value here as entered by the user previously
    the_radius = Decimal(the_radius)
    #user will enter the height value here of the right circular cylinder
    while not the_height:
        the_height = input('Enter the height value (must be a positive number): ')
        if not the_height.isdecimal():
            the_height = None
        if not Decimal(the_height) > 0:
            the_height = None
    #setting the height value here as entered by the user previously
    the_height = Decimal(the_height)
    #returning the radius value and height value of the right circular
    #cylinder as entered by the user
    return the_radius, the_height
def calculation_right_cylinder_arguments(arguments):
    """ This function is designed to get the parameters entered by the
    user of the radius and height of the right circular cylinder when
    selecting this menu option at the start of program """
    the_radius, the_height = arguments
    #returning the calculated right circular cylinder value here
    #using the volume formula of the right circular cylinder as needed
    return Decimal((Decimal(math.pi) * the_radius ** 2) * the_height)
def total_days_from_07042025():
    """ This function is used to calculate the number of days
    there is left to reach the date of July 4, 2025 """
    #the target date to reach as noted for the menu option
    number_of_days = date(2025, 7, 4)
    #the date today which is the current starting point, as it
    #changes as the days keep getting closer to the target date
    today_date = date.today()
    #getting the total number of days to reach the target date
    #calculation will be done here
    delta = (number_of_days - today_date)
    #returning the number of days to reach the target date of
    #July 4, 2025
    return delta.days
def main():
    """ This is the function of the main program which will start
    the main program execution such as, allowing the user to
    see the displayed menu of a set of options to choose from,
    and processing the information of the option as selected
    accordingly """
    user_choice = None
    #as long as user does not enter option f to terminate program
    #exection, the program will keep allowing the user to select the
    #option from a-e which starts from generating a secure password and
    #goes until calculating the volume of a right circular cylinder
    while user_choice != 'f':
        #displaying the menu options needed for user to select the
        #option wanted for using the program effectively as possible
        displaying_menu()
        #user choice will be processed here and stored
        user_choice = user_entering_option()
        #if user selects choice a of generating a secure password
        #the following will get to process and run
        if user_choice == 'a':
            secure_password_arguments = securing_password()
            final_password_display = sending_params_secure_password(secure_password_arguments)
            #printed result of the generated secure password as wanted by user and formatted
            #properly
            print(f"Your Secure Password is: {final_password_display}\n")
        #if the user selects choice b of calculating and formatting a
        #decimal percentage, the following will process and run
        elif user_choice == 'b':
            number_aspercentage = calculate_and_format_percentage()
            final_percentage = calculating_and_format_percentage(number_aspercentage)
            #printed result of the calculated and formatted percentage number as wanted by
            #user and formatted properly
            print(f'Your Percentage is: {final_percentage}\n')
        #if the user selects choice c of getting the total days until
        #the date of July 4, 2025, the following will process and run
        elif user_choice == 'c':
            total_days = total_days_from_07042025()
            #printed result of the number of days until the date of
            #July 4, 2025 as wanted by the user and formatted properly
            print(f'The days until July 4, 2025 is: {total_days}\n')
        #if the user selects choice d of using the law of cosines to find
        #the calculated c side of the triangle, the following will process
        #and run
        elif user_choice == 'd':
            solving_c = calculation_law_cosines()
            final_calculation_of_c = the_calculation_law_cosines(solving_c)
            #printed result of the length of the c side of the triangle calculated
            #using the law of cosines as wanted by the user and formatted
            #properly
            print(f'The length of leg C is: {final_calculation_of_c}\n')
        #if the user selects choice e of calculating the volume of the
        #right circular cylinder, the following will process and run
        elif user_choice == 'e':
            getting_right_cylinder = calculation_right_cylinder()
            final_volume_calculated = calculation_right_cylinder_arguments(getting_right_cylinder)
            #printed result of the calculated volume of the right circular
            #cylinder as wanted by the user and formatted properly
            print(f"The Cylinder's Volume is: {final_volume_calculated}\n")
        #if the user selects choice f of exiting and terminating
        #program execution, a thank you message will be printed to the
        #screen for trying out the program and the program will exit out as needed
        elif user_choice == 'f':
            print('Thank you for trying out this application.')
main()
