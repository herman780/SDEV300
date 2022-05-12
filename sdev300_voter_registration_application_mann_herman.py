# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 16:16:53 2022

@author: Herman Mann
"""
def check_exiting_voter_registration():
    """ This function allows the user to exit out of the
    program and cancel the process of registering to vote at any time.
    The user will enter either a Yes to keep continuing the process of
    registering, or No if the user wants to exit and stop the registration
    process. If the user enters Yes, the program will return true and keep
    the registration process going until anything else (such as No) is
    encountered and which will then return false. """
    #gives user the option at any time in the program to exit the program
    #and cancel the registration process.
    user_input = input("Do you want to continue with Voter Registration? \n")
    user_input = user_input.lower() #converts upper case to lower case
    if user_input == "yes":
        return 1
    return 0
def get_the_state():
    """ This function is set up for the user to input the state of where
    user is located at the time of the voting registration process. If the
    length of the state is more than two letters, then the program will make
    the user enter a valid U.S. state consisted of a maximum of only two letters. If
    the user chooses to exit before entering the state for the requirement of the
    voting process then the program will return exit to exit out of the program. """
    while 1:
        if not check_exiting_voter_registration():
            return "exit"
        # user will input a valid U.S. state consisted of two letters at maximum
        # for the voting registration process.
        state = input("What state do you live? \n")
        if checking_alphabetic_validation(state):
            state = state.lower() #converts upper case to lower case
            #if the length of the entered state by user is two letters
            #the program will return the state of the user entered choice, and
            #will let the program continue with the voting registration process
            #until user chooses to exit out.
            if len(state) == 2:
                return state
def checking_alphabetic_validation(string_entered):
    """ This function is designed to make sure whenever the user
    enters or inputs a string which consists of either the user's state, first
    and last name, etc and that it consists of only alphbetical letters,
    and nothing else. """
    #checking to make sure that the string is alphabet only as required.
    #returns true if string entered by user is alphabet letters
    #and false otherwise.
    if string_entered.isalpha():
        return True
    return False
def get_user_name(starting_message):
    """ This function is used for getting the user's first and last name
    when the user inputs it as the requirement for the voting registration
    process. If user chooses to exit before entering either the first or
    last name, the program will stop and exit. """
    while 1:
        if not check_exiting_voter_registration():
            return "exit" #returns exit if user chooses not to enter name (first or last)
        name_of_user = input(starting_message) #getting the user's first name and last name
        #if the user's first and last name contains alphabet letters, program will return
        #the name of the user.
        if checking_alphabetic_validation(name_of_user):
            return name_of_user
def get_user_country():
    """ This function is designed to get the user's country and specifically
    makes sure that the user is a U.S. citizen or not. If user chooses to
    exit before entering an option for the country, then the program will exit
    out. The user will input their country as a requirement of the voting
    registration process. If user enters No which means they are not a U.S. citizen,
    the remaining questions of the voting registration process won't be shown and the program
    will exit out. """
    while 1:
        if not check_exiting_voter_registration():
            return "exit"
        #user will input if they are a U.S. citizen as a requirement for the
        #voting registration process, either by entering Yes or No.
        country = input("Are you a U.S. Citizen? \n")
        #if the user enters a string of country which contains alphabet letters
        #then program will keep continuing on depending on if user enters Yes
        #or a little later.
        if checking_alphabetic_validation(country):
            country = country.lower() #converts upper case to lower case
            #if user is U.S. citizen the program will return yes.
            if country == "yes":
                return "yes"
            #if user is not a U.S. citizen the program will return no
            #and will be made to exit out of the voting registration process.
            return "no"
def get_user_age():
    """ This function is designed to get the user's age as part of the
    voting registration process. If user chooses to exit before entering the
    age, then the program will be made to exit out and terminate execution which
    means it will return -1. A try and excepion clause will be used to check if
    the user entered the appropriate age which is part of the voting registration
    process requirement. If the user enters an age that is less than 18 years old,
    or greater than 120 years old the program will terminate if user enters an age
    less than 18 years old, but if user enters an age greater than 120 years old,
    the user would have the option to input their age again. """
    while 1:
        #if user chooses to exit out of program before entering their age,
        #the program will return -1, and will then terminate out of entirety
        #of program.
        if not check_exiting_voter_registration():
            return -1
        try:
            #user will input their age for voting registration process
            name_of_user_ = input("What is your age? \n")
            age_of_user = int(name_of_user_)
            #if the user enters an age less than 18 years old
            #then a print statement will be printed out to screen allowing
            #the user another chance to enter the appropriate age needed for
            #the voting registration process.
            if age_of_user < 18:
                name_of_user_ = input("Are you at least 18 years old? \n")
                name_of_user_ = name_of_user_.lower() #converts upper case to lower case
            #if user enters an age greater than 120 years old
            #print statement will be printed to screen which would state the
            #requirement of the age to be in between for the voting registration
            #process
            elif age_of_user > 120:
                print("\nAre you older than 120 years old?")
                print("If so, the permittable age to vote can")
                print("only be between 18 and 120 years old.")
                name_of_user_ = name_of_user_.lower() #converts upper case to lower case
            if age_of_user >= 18:
                if age_of_user <= 120:
                    return age_of_user
            if name_of_user_ == "no":
                return -1
        #Exception ValueError will be defined if user does not enter the permittable
        #age needed for meeting the requirement of the voting registration process.
        except ValueError:
            pass
def get_user_zipcode():
    """ This function is designed to get the user's zipcode which is needed
    for the voter registration process. If user chooses to exit before entering
    the zipcode by entering a No or anything else, the program will terminate and
    exit out. A try and except clause will be used to make sure the user enters
    an appropriate zipcode containing the minimum and maximum of five digits.
    An except ValueError will be defined if user does not enter the appropriate
    zipcode as part of the requirements for the voting registration process. """
    while 1:
        #If user chooses to exit before entering the zipcode which is part of the
        #voting registration process, then the program will return -1.
        if not check_exiting_voter_registration():
            return -1
        #A try and except clause will be used to prove logical validity
        #of the appropriate entered zipcode by the user which would be entered
        #as input and is made sure it has five digits.
        try:
            #user inputs five digit zipcode here as part of the voting
            #registration process.
            user_zip_code = input("What is your zipcode? \n")
            #if user enters the appropriate zipcode length of five digits
            #the zipcode entered by the user will be returned successfully
            if len(user_zip_code) == 5:
                return int(user_zip_code)
        #Except clause will be used if zipcode does not meet the requirements
        #of the necessary requirement of the voting registration process.
        except ValueError:
            pass
#Start of processing of the overall voting registration process data.
if __name__ == "__main__":
    print("**********************************************************************")
    print("Welcome to the Python Voter Registration Application.")
    USER_VOTER = []
    while 1:
        #User's first name will have to be inputted and by chance if
        #the first name entered by the user is exit, the program will
        #terminate.
        USERFIRSTNAME = get_user_name("What is your first name? \n")
        if USERFIRSTNAME == "exit":
            break
        #Adding towards the end of the list of the required fields
        #of the voting registration process of the
        #user's first name information which will be outputted to the screen.
        USER_VOTER.append(USERFIRSTNAME)
        #User's last name will have to be inputted and by chance if
        #the last name entered by the user is exit, the program will
        #terminate.
        USERLASTNAME = get_user_name("What is your last name? \n")
        if USERLASTNAME == "exit":
            break
        #Adding towards the end of the list of the required fields
        #of the voting registration process of the user's last name
        #information which will be outputted to the screen.
        USER_VOTER.append(USERLASTNAME)
        #Getting the user's age which has to be inputted
        #and by chance if the user enters -1 for the age,
        #the program will terminate. Since it is a sentinal
        #value to terminate program's execution.
        USERAGE = get_user_age()
        if USERAGE == -1:
            break
        #Adding the user's age towards the end of the list of the
        #required fields of the voting registration process of the user's
        #age information which will be outputted to the screen.
        USER_VOTER.append(USERAGE)
        #The user's country will have to be inputted as a yes or no,
        #to determine if the user is a U.S. citizen or not.
        USERCOUNTRY = get_user_country()
        if USERCOUNTRY in ('exit', 'no'):
            break
        #Adding the user's citizen status towards the end of the
        #list of the required fields of the voting registration
        #process.
        USER_VOTER.append("Yes")
        #The user will have to input the state as requirement of
        #the voting registration process. If user chooses to enter
        #exit then the program will terminate.
        USERSTATE = get_the_state()
        if USERSTATE == "exit":
            break
        #Adding the user's state towards the end of the list
        #as needed for outputting the voting registration process.
        USER_VOTER.append(USERSTATE.upper())
        #User will input their zipcode, and if user chooses to input
        #-1 for zipcode, or anything that does not meet requirements of
        #the zipcode requirement of the voting registration process program
        #will terminate.
        USERZIPCODE = get_user_zipcode()
        if USERZIPCODE == -1:
            break
        #Adding towards the end of the required fields of the voting
        #registration process list, the user's entered zipcode.
        USER_VOTER.append(USERZIPCODE)
        #if all of the required fields of the voting registration
        #process is satisfied, the information will be printed to the
        #screen as output based upon what the user inputs.
        if len(USER_VOTER) == 6:
            print("\nThanks for registering to vote.")
            #information will be outputted starting now.
            print("Here is the information we received: ")
            #User's first and last name will be outputted to the screen
            print("Name (first last):", USER_VOTER[0], USER_VOTER[1])
            #User's age is outputted to the screen based on what user has
            #entered.
            print("Age:", USER_VOTER[2])
            #The status of the user if the user is a U.S. citizen
            #is outputted to the screen.
            print("U.S. Citizen:", USER_VOTER[3])
            #The user's state at the time for completing the
            #voting registration process will be outputted to the screen.
            print("State: ", USER_VOTER[4])
            #User's zipcode is outputted to the screen.
            print("Zipcode: ", USER_VOTER[5])
            #All information is outputted to the screen. Then a thank you
            #message is outputted to the screen and depending on if the
            #user chooses to restart again the user can then choose to do so.
            print("Thanks for trying the Voter Registration Application.")
            print("Your voter registration card should be shipped within 3 weeks.")
            print("**********************************************************************")
    