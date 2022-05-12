# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:20:53 2022
Lab 4: Numpy and Pandas Application Program
@author: Herman Mann
"""
#necessary imports for completion of lab
import sys
import re
import numpy as np_option

#used for regular expression of valid phone number format
PHONE_FORMAT =  r"^[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4}$"
#used for regular expression of valid zipcode format
ZIP_CODE_FORMAT = r"\d{5}-\d{4}"
#used for exiting program if chosen by user
NUMBER_SIGN = "*"*10
#### Start of Numpy and Pandas Application Program Execution ####
print("\n**************** Welcome to the Python Matrix Application *************\n")
#User will input either Y or N if wants to continue with game
print("Do you want to play the Matrix Game? ")
yes_or_no_input = input("Enter Y for Yes or N for No: \n")
#If user does not want to continue a thank you message will print
#and program will exit
if yes_or_no_input in ('N', 'n'):
    print("\n************** Thanks for playing Python Numpy **************")
    sys.exit()
def valid_phone_number(phone_number):
    """ This function is used for defining a valid phone number format
    using regular expressions as necessary to do so """
    return re.fullmatch(PHONE_FORMAT, phone_number)

def valid_zipcode(zip_code):
    """ This function is used for defining a valid zip code format
    using regular expressions as necessary to do so """
    return re.fullmatch(ZIP_CODE_FORMAT, zip_code)

#If user wants to continue with program the following will then be
#executed as expected
if yes_or_no_input in ('Y', 'y'):
    #Entering of phone number
    user_phone = input("Enter your phone number (XXX-XXX-XXXX): \n")
    while not valid_phone_number(user_phone):
        #if user phone number not valid, user has to retry in correct
        #format
        user_phone = input("\nYour phone number is not in correct format. Please reenter: \n")
    zipcode = input("Enter your zip code+4 (XXXXX-XXXX): \n")
    while not valid_zipcode(zipcode):
        #if user zipcode is not valid, the user will be given another
        #chance to reenter the zipcode in proper format
        zipcode = input("\nYour zip code is not in correct format. Please reenter: \n")
# Start of user entering values of the two 3x3 matrices, and then
# selecting from the options of addition, subtraction, matrix
# multiplication, and element by element multiplication
    first_Matrix = []
    the_second_Matrix = []

    #### Beginning of first 3x3 matrix to be inputted (total of 9 numbers, one by one) ####
    print("\nEnter your first 3x3 matrix: ")
    #used for formatting the rows of the two matrixes needed to be
    #entered
    for number_of_rows in range(3):
        row_for_matrix1 = []
        for number_of_columns in range(3):
            row_for_matrix1.append(int(input()))
        first_Matrix.append(row_for_matrix1)
    #The first matrix will be printed to the screen
    print("\nYour first 3x3 matrix is: \n")
    for j in range(3):
        for k in range(1):
            SPACING_PURPOSES = " "
            print(SPACING_PURPOSES.join(map(str, first_Matrix[j+k])))
    #### Beginning of second 3x3 matrix to be inputted (total of 9 numbers, one by one) ####
    print("\nEnter your second 3x3 matrix: ")
    for number_of_rows in range(3):
        row_for_matrix2 = []
        for number_of_columns in range(3):
            row_for_matrix2.append(int(input()))
        the_second_Matrix.append(row_for_matrix2)
    print("\nYour second 3x3 matrix is: \n")
    for j in range(3):
        for k in range(1):
            MATRIX_2_SPACING_PURPOSES = " "
            print(MATRIX_2_SPACING_PURPOSES.join(map(str, the_second_Matrix[j+k])))
    # Beginning of Selecting the options from either Addition, Subtraction
    # matrix multiplication, and element by element multiplication.
    print("\nSelect a Matrix Operation from the list below: \n")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Matrix Multiplication")
    print("d. Element by element multiplication")
    print("e. Quitting the program")
    user_option = input()
    #Addition option of the matrixes
    if user_option == 'a':
        adding_matrix1_matrix2 = np_option.add(first_Matrix, the_second_Matrix)
        adding_option_transpose = np_option.transpose(adding_matrix1_matrix2)
        print("\nYou selected Addition. The results are: \n")
        for j in range(3):
            for k in range(1):
                SPACING_PURPOSES = " "
                print(SPACING_PURPOSES.join(map(str, adding_matrix1_matrix2[j+k])))
        print("\nThe Transpose is: \n")
        for j in range(3):
            for k in range(1):
                SPACING_PURPOSES = " "
                print(SPACING_PURPOSES.join(map(str, adding_option_transpose[j+k])))
        np_option.set_printoptions(precision=2)
        print("\nThe row and column mean values of the results are: \n")
        print("Row:", np_option.mean(adding_matrix1_matrix2, axis=1))
        print("Column:", np_option.mean(adding_matrix1_matrix2, axis=0))
    #Subtraction option of the matrixes
    elif user_option == 'b':
        #### Beginning of the Subtraction option of the matrixes ####
        subtracting_matrix1_matrix2 = np_option.subtract(first_Matrix, the_second_Matrix)
        subtracting_option_transpose = np_option.transpose(subtracting_matrix1_matrix2)
        print("\nYou selected Subtraction. The results are: \n")
        for j in range(3):
            for k in range(1):
                SPACING_PURPOSES = " "
                print(SPACING_PURPOSES.join(map(str, subtracting_matrix1_matrix2[j+k])))
        print("\nThe Transpose is: \n")
        for j in range(3):
            for k in range(1):
                SPACING_PURPOSES = " "
                print(SPACING_PURPOSES.join(map(str, subtracting_option_transpose[j+k])))
        np_option.set_printoptions(precision=2)
        print("\nThe row and column mean values of the results are: \n")
        print("Row:", np_option.mean(subtracting_matrix1_matrix2, axis = 1))
        print("Column:", np_option.mean(subtracting_matrix1_matrix2, axis = 0))
    #Multiplication of matrixes option
    elif user_option == 'c':
        #### Beginning of Matrix Multiplication ####
        matrixes_multiplication = np_option.matmul(first_Matrix, the_second_Matrix)
        matrix_multiplication_transpose = np_option.transpose(matrixes_multiplication)
        print("\nYou selected Matrix Multiplication. The results are: \n")
        for j in range(3):
            for k in range(1):
                SPACING_PURPOSES = " "
                print(SPACING_PURPOSES.join(map(str, matrixes_multiplication[j+k])))
        print("\nThe Transpose is: \n")
        for j in range(3):
            for k in range(1):
                SPACING_PURPOSES = " "
                print(SPACING_PURPOSES.join(map(str, matrix_multiplication_transpose[j+k])))
        np_option.set_printoptions(precision=2)
        print("\nThe row and column mean values of the results are: \n")
        print("Row:", np_option.mean(matrixes_multiplication, axis = 1))
        print("Column:", np_option.mean(matrixes_multiplication, axis = 0))
    #Element by element multiplication option
    elif user_option == 'd':
        #### Beginning of the Element by element multiplication ####
        #### process of both of the matrixes ####
        element_by_element_mul = np_option.multiply(first_Matrix, the_second_Matrix)
        ele_by_ele_mul_transpose = np_option.transpose(element_by_element_mul)
        print("\nYou selected Element by element multiplication. The results are: \n")
        for j in range(3):
            for k in range(1):
                SPACING_PURPOSES = " "
                print(SPACING_PURPOSES.join(map(str, element_by_element_mul[j+k])))
        print("\nThe Transpose is: \n")
        for j in range(3):
            for k in range(1):
                SPACING_PURPOSES = " "
                print(SPACING_PURPOSES.join(map(str, ele_by_ele_mul_transpose[j+k])))
        np_option.set_printoptions(precision=2)
        print("\nThe row and column mean values of the results are: \n")
        print("Row:", np_option.mean(element_by_element_mul, axis = 1))
        print("Column:", np_option.mean(element_by_element_mul, axis = 0))
    #option to exit for user after program is done
    elif user_option == 'e':
        print()
        print(NUMBER_SIGN + " Thank you for testing the Numpy and Pandas program " +
              NUMBER_SIGN)
    else:
        print("\nInvalid option entered, please try again. ")
        
