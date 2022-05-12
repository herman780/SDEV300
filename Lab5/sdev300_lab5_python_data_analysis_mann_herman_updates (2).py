# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 17:37:05 2022
Lab 5: Python Data Analysis
@author: Herman Mann
"""
#Importing all the necessary modules needed for this program
import sys
#Needed for the printing of the statistical data
import pandas as pd
#Needed for displaying the histogram of the population and
#housing data plots based on the information from the csv files
from matplotlib import pyplot as plt
### This program allows a user to load one of the two CSV files and then
### perform histogram analysis and plots for select variables on the datasets.
### The first dataset represents the population change for specific dates
### for U.S. regions. The second dataset represents Housing data over an
### extended period of time describing home age, number of bedrooms and other
### variables. The first row provides a column name for each dataset. The
### following columns should be used to perform analysis:
    ## PopChange.csv:
      # Pop Apr 1
      # Pop Jul 1
      # Change Pop
    ## Housing.csv:
      # AGE
      # BEDRMS
      # BUILT
      # ROOMS
      # UTILITY
      # WEIGHT
      # NUNITS
### Specific statistics should include:
      # Count
      # Mean
      # Standard Deviation
      # Min
      # Max
      # Histogram
def population_data_print_data(dataframe_read):
    """ This function is designed to analyze the population change
    for specific dates for U.S. regions and will print a histogram
    of each of the specific dates population change, and along the
    histogram of the the changed population due to the factors of the
    changes of specific dates of U.S. regions """
    #Needed for the upper and lower points of the histogram to
    #prevent the outliers from being entered within the calculation
    #of the data
    bottom_quantile = .20
    upper_quantile = .90
    #Copying elements from the called function
    pop_data_analysis = dataframe_read
    user_selection_option = False
    column_num = -1
    print("Select the Column you want to analyze:")
    print("a.", pop_data_analysis.columns[4])
    print("b.", pop_data_analysis.columns[5])
    print("c.", pop_data_analysis.columns[6])
    print("d. Exit Column")
    #User will input the choice here
    user_input = input().lower()
    while not user_selection_option:
        #Pop Apr 1 option if user chooses to select
        if user_input == 'a':
            user_selection_option = True
            column_num = 4
        #Pop Jul 1 option if user chooses to select
        elif user_input == 'b':
            user_selection_option = True
            column_num = 5
        #Changing population (Change Pop) option if user chooses to select
        elif user_input == 'c':
            user_selection_option = True
            column_num = 6
        #Exiting the column option for the population data csv file
        #to then return back to the main menu.
        elif user_input == 'd':
            user_selection_option = True
            print("You selected to exit the column menu")
        #If user enters any other option, the following will be displayed
        #to the screen
        else:
            #print("Inappropriate entry is detected, enter a letter between (a-d).")
            input("Hit <ENTER> to continue....")
            main()
    #If the column number of the data is not -1, the statisitcal information
    #of the population data would be printed along with the histogram plot
    if column_num != -1:
        print("You selected {}".format(pop_data_analysis.columns[column_num].title()))
        print("The statistics for this column are:")
        print(pop_data_analysis.describe()[pop_data_analysis.columns[column_num]].apply(
              lambda value: format(value, '.2f')))
        number_bins = 20
        bins = [pop_data_analysis[pop_data_analysis.columns[column_num]].quantile(
                total / number_bins)
                 for total in range(number_bins)
                      if bottom_quantile < (total / number_bins) < upper_quantile]
        bins.sort()
        pop_data_analysis.hist(column = pop_data_analysis.columns[column_num], rwidth=.5,
                               bins = bins, edgecolor = 'black')
        plt.xlim(
        [pop_data_analysis[pop_data_analysis.columns[column_num]].quantile(bottom_quantile),
         pop_data_analysis[pop_data_analysis.columns[column_num]].quantile(upper_quantile)])
        #The x label of the population data histogram plot
        plt.xlabel(pop_data_analysis.columns[column_num], fontsize = 12)
        #The y label of the population data histogram plot
        plt.ylabel("Occurrences of x-values", fontsize = 12)
        #The title of the population data histogram plot
        plt.title("Data of Population Change Histogram")
        print("The Histogram of this column is now displayed.")
        #Used for displaying the histogram of the population data.
        plt.show()
def housing_data_analysis(dataframe_housing_read):
    """ This function is used for analyzing the housing data
    over an extended period of time describing home age,
    utilities and their costs, the number of rooms, and many
    other variables. Will display a histogram based on the data
    of each of the variables as they represent different columns """
    #used for printing the data associated with housing.csv
    #and to display the histogram later on
    column_num = -1
    pop_data_house = dataframe_housing_read
    #used for selecting the appropriate option of housing variables
    #to choose from
    user_option_house_var = False
    #label for the various variables for describing the house
    #such as the age, number of bedrooms, and much more
    variable_label = ""
    #This is used to print the dictionary list of items starting from
    # the age until the exit column option for the housing data
    #csv file.
    print("There are a variety of columns to analyze:")
    #the dictionary list of the housing data csv file needed to be processed
    #and executed.
    housing_menu_items = {
        1: "AGE",
        2: "BEDRMS",
        3: "BUILT",
        4: "NUNITS",
        5: "ROOMS",
        6: "WEIGHT",
        7: "UTILITY",
        8: "EXIT COLUMN",
    }
    for menu_option in housing_menu_items.keys():
        print(menu_option, "\t", housing_menu_items[menu_option])
    user_house_var_input = int(input("Select the Column you want to analyze: \t"))
    while not user_option_house_var:
        #If the user chooses to go with the option "AGE" for the housing
        #data, then the following would be able to execute
        if user_house_var_input == 1:
            user_option_house_var = True
            #The column number is of index 0 in the housing data csv file
            column_num = 0
            variable_label = "Age of House"
        #if the user chooses to go with the "BEDRMS" option the following
        #will be executed
        elif user_house_var_input == 2:
            user_option_house_var = True
            #The column number is of index 1 in the housing data csv file
            column_num = 1
            variable_label = "BEDROOMS"
        #if the user chooses to go with the "BUILT" option the following will
        #be executed
        elif user_house_var_input == 3:
            user_option_house_var = True
            column_num = 2
            variable_label = "Year Built"
        #If the user chooses to go with the "NUNITS" option the following
        #will be able to execute.
        elif user_house_var_input == 4:
            user_option_house_var = True
            column_num = 3
            variable_label = "Number of Units"
        #If the user chooses to go with the number of rooms option, the
        #following will be able to execute
        elif user_house_var_input == 5:
            user_option_house_var = True
            column_num = 4
            variable_label = "Number of Rooms"
        elif user_house_var_input == 6:
            user_option_house_var = True
            column_num = 5
            variable_label = "Weight"
        elif user_house_var_input == 7:
            user_option_house_var = True
            column_num = 6
            variable_label = "UTILITY COSTS ($) and types of Utilities"
        elif user_house_var_input == 8:
            user_option_house_var = True
            print("You selected to exit the column menu")
        #If the user enters an invalid entry then the following will be
        #executed and the message will be printed to the screen.
        else:
            print("That is not a valid entry. Column entry must be between (1-8)")
            input("Hit <ENTER> to continue....\n")
            main()
    #Used for displaying the statistics and histogram of the housing data
    if column_num != -1:
        print("You selected {}".format(pop_data_house.columns[column_num].title()))
        print("The statistics for this column are:")
        print(pop_data_house.describe()[pop_data_house.columns[column_num]].apply(
            lambda house_val: format(house_val, '.2f')))
        pop_data_house.hist(column = pop_data_house.columns[column_num], rwidth = 0.4,
                            bins = 15)
        plt.xlabel(variable_label, fontsize=12)
        plt.ylabel("The number/quantity built", fontsize=12)
        plt.title("The Housing Data over an extended period of time")
        print("The Histogram of this column is now displayed.")
        plt.show()
        input("Hit <ENTER> to continue....\n")
def main():
    """ This function is the main function, and all of the code will
    be executed through here. Allows the user to select from either
    the housing data csv file or population data csv file, and displays
    a set of three options to choose from for then later on displaying the
    statistical data and along that the histogram plot """
    #initializing the main header of the overall program
    main_header = "*************** Welcome to the Python Data Analysis App ***************** "
    thankyou_message_option3 = "************* Thanks for using the Data Analysis App ************"
    #defining of the 2 needed csv files
    population_data = "PopChange.csv"
    housing_data = "Housing.csv"
    #If anything is not true according to the current state of program
    #then following won't execute or print, otherwise it will.
    #Printing of title header (the main header upon entry in program)
    print(main_header)
    while True:
        #printing of appropriate options for the user to choose from
        print("Select the file you want to analyze:")
        print("1. Population Data")
        print("2. Housing Data")
        print("3. Exit the Program")
        #The user will enter the input from (1-3).
        user_input = input()
        #If the user enters option 1, the population data would be executed
        if user_input == "1":
            print("You have entered Population Data.")
            #Trying to read the PopChange.csv file (population data file)
            try:
                dataframe_population_read = pd.read_csv(population_data)
                population_data_print_data(dataframe_population_read)
            #If the file could not be read, the following errors would be
            #presented
            except (FileNotFoundError, IOError):
                #Following message will be printed/displayed
                print("Error in attempting to read file")
                #The input will be used for entering the main menu again.
                input("Hit <ENTER> to continue with the program execution....")
        #If the user enters option 2, the housing data csv file would be
        #executed, and the following information would be executed and
        #used.
        elif user_input == "2":
            print("You have entered Housing Data.")
            #Trying to read the Housing.csv file which contains the
            #data of the house variables such as the number of rooms,
            #the utilities, the age of the house, weight, and much more
            try:
                dataframe_housing_read = pd.read_csv(housing_data)
                housing_data_analysis(dataframe_housing_read)
            #If the file could not be read, the following errors would be
            #presented
            except (FileNotFoundError, IOError):
                print("Error in attempting to read file")
                input("Hit <ENTER> to continue with the program execution....")
        #If the user enters option 3, the program will exit/terminate
        #and will display the thank you message
        elif user_input == "3":
            print()
            print(thankyou_message_option3)
            break
        else:
            print("Inappropriate entry detected.")
            input("Hit <ENTER> to continue....")
    #Exiting from the program, and halting program execution
    sys.exit(0)
#Calling of the main function to print the information and start program
#execution
main()

####################### END OF PROGRAM #########################
