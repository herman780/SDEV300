# -*- coding: utf-8 -*-
"""
Created on Wed Apr 6 00:53:35 2022

Lab 3: Python State Capital and Flower List Application program

@author: Herman Mann
"""

#Importing the appropriate needed packages for successful
#program execution
import sys
#Used for the flower images to display them for each of the 50 associated
#states
from io import BytesIO
#needed for getting the requests of getting the link of the flower from
#the internet of each associated state
import requests
#Needed for displaying every associated images of the state's flowers
from PIL import Image
#needed for developing the bar graph for option 3
import matplotlib.pyplot as plt

###### Adding Each state's information starting with the state's name, state's capital
###### Followed along with the state's population, the state's flower, and finally
###### the link of the associated flower representing the associated flower of each state
state_information = []
#Appending each state to the list to be displayed later on, after adding
#state by state
state_information.append(['Alabama', 'Montgomery', 4949697, 'Camellia',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/camellia-flower.jpg'''])
state_information.append(['Alaska', 'Juneau', 720763, 'Forget Me Not',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/Alpineforgetmenot.jpg'''])
state_information.append(['Arizona', 'Phoenix', 7640796, 'Saguaro Cactus Blossom',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
saguaroflowersFlickr.jpg'''])
state_information.append(['Arkansas', 'Little Rock', 3042017, 'Apple Blossom',
'''https://statesymbolsusa.org/sites/\
statesymbolsusa.org/files/primary-images/AppletreeblossomArkansasflower.JPG'''])
state_information.append(['California', 'Sacramento', 39664128, 'California Poppy',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/CAflowerCaliforniaPoppy.jpg'''])
state_information.append(['Colorado', 'Denver', 5826185, 'Rocky Mountain Columbine',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
Colorado_columbine2.jpg'''])
state_information.append(['Connecticut', 'Hartford', '3559054', 'Mountain Laurel',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/\
Mountain-Laural-flowers2.jpg'''])
state_information.append(['Delaware', 'Dover', 982049, 'Peach Blossom',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/\
peachblossomspeachflowers.jpg'''])
state_information.append(['Florida', 'Tallahassee', 21711157, 'Orange Blossom',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/OrangeBlossomsFloridaFlower.jpg'''])
state_information.append(['Georgia', 'Atlanta', 10723715, 'Cherokee Rose',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/CherokeeRoseFlower.jpg'''])
state_information.append(['Hawaii', 'Honolulu', 1411151, 'Yellow hibiscus brackenridgei',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/yellowhibiscusPuaAloalo.jpg'''])
state_information.append(['Idaho', 'Boise', 1823594, 'Syringa',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/syringaPhiladelphuslewisiiflower.jpg'''])
state_information.append(['Illinois', 'Springfield', 12620571, 'Violet',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/singlebluevioletflower.jpg'''])
state_information.append(['Indiana', 'Indianapolis', 6768941, 'Peony',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/PeonyPaeoniaflowers.jpg'''])
state_information.append(['Iowa', 'Des Moines', 3161522, 'Wild Rose',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/WildPrairieRose.jpg'''])
state_information.append(['Kansas', 'Topeka', 2915269, 'Wild Native Sunflower',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/native-sunflowers.jpg'''])
state_information.append(['Kentucky', 'Frankfort', 4474193, 'Goldenrod',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/stateflowergoldenrod-bloom.jpg'''])
state_information.append(['Louisiana', 'Baton Rouge', 4637898, 'Magnolia',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/MagnoliagrandifloraMagnoliaflower.jpg'''])
state_information.append(['Maine', 'Augusta', 1349367, 'White Pine Cone and Tassel',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/whitepinemalecones.jpg'''])
state_information.append(['Maryland', 'Annapolis', 6055558, 'Black-Eyed Susan',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/FlowerMDBlack-eyedSusan.jpg'''])
state_information.append(['Massachusetts', 'Boston', 6902371, 'Mayflower',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/MayflowerTrailingArbutus.jpg'''])
state_information.append(['Michigan', 'Lansing', 9989642, 'Apple Blossom',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/appleblossombeauty.jpg'''])
state_information.append(['Minnesota', 'Saint Paul', 5673015, 'Pink & White Lady Slipper',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/pinkwhiteladysslipperflower1.jpg'''])
state_information.append(['Mississippi', 'Jackson', 2971278, 'Magnolia',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/magnoliablossomflower01.jpg'''])
state_information.append(['Missouri', 'Jefferson City', 6153233, 'White Hawthorn Blossom',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/hawthornflowersblossoms1.jpg'''])
state_information.append(['Montana', 'Helena', 1076891, 'Bitterroot',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/bitterrootfloweremblem.jpg'''])
state_information.append(['Nebraska', 'Lincoln', 1943202, 'Goldenrod',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/goldenrodflowersyellow4.jpg'''])
state_information.append(['Nevada', 'Carson City', 3132971, 'Sagebrush',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/Nevada-Sagebrush-Artemisia-tridentata.jpg'''])
state_information.append(['New Hampshire', 'Concord', 1365957, 'Purple Lilac',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/lilacflowerspurplelilac.jpg'''])
state_information.append(['New Jersey', 'Trenton', 8878355, 'Violet',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
wood-violet.jpg'''])
state_information.append(['New Mexico', 'Santa Fe', 2100917, 'Yucca',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/YuccaFlowersclose.jpg'''])
state_information.append(['New York', 'Albany', 19376771, 'Rose',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/redrosebeautystateflowerNY.jpg'''])
state_information.append(['North Carolina', 'Raleigh', 10594553, 'Dogwood',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/floweringdogwoodflowers2.jpg'''])
state_information.append(['North Dakota', 'Bismarck', 766044, 'Wild Prairie Rose',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/flowerwildprairierose.jpg'''])
state_information.append(['Ohio', 'Columbus', 11701859, 'Red Carnation',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/redcarnationOhioflower.jpg'''])
state_information.append(['Oklahoma', 'Oklahoma City', 3973707, 'Mistletoe',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/mistletoe_phoradendron_serotinum.jpg'''])
state_information.append(['Oregon', 'Salem', 4253588, 'Oregon Grape',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/Oregongrapeflowers2.jpg'''])
state_information.append(['Pennsylvania', 'Harrisburg', 12803056, 'Mountain Laurel',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
Mt_Laurel_Kalmia_Latifolia.jpg'''])
state_information.append(['Rhode Island', 'Providence', 1060435, 'Violet',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/violetsflowers.jpg'''])
state_information.append(['South Carolina', 'Columbia', 5213272, 'Yellow Jessamine',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/CarolinaYellowJessamine101.jpg'''])
state_information.append(['South Dakota', 'Pierre', 890620, 'American Pasque',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/Pasqueflower-03.jpg'''])
state_information.append(['Tennessee', 'Nashville', 6886717, 'Passion Flower',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/passionflowerwildflower2.jpg'''])
state_information.append(['Texas', 'Austin', 29363096, 'Bluebonnet',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/BluebonnetsBlueRed.jpg'''])
state_information.append(['Utah', 'Salt Lake City', 3258366, 'Sego Lily',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
SegoLily.jpg'''])
state_information.append(['Vermont', 'Montpelier', 623620, 'Red Clover',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/redcloverstateflowerWV.jpg'''])
state_information.append(['Virginia', 'Richmond', 8569752, 'American Dogwood',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/floweringDogwoodSpring.jpg'''])
state_information.append(['Washington', 'Olympia', 7705917, 'Coast Rhododendron',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/flower_rhododendronWeb.jpg'''])
state_information.append(['West Virginia', 'Charleston', 1780003, 'Rhododendron',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/rhododendronWVstateflower.jpg'''])
state_information.append(['Wisconsin', 'Madison', 5837462, 'Wood Violet',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
wood-violet.jpg'''])
state_information.append(['Wyoming', 'Cheyenne', 579917, 'Indian Paintbrush',
'''https://statesymbolsusa.org/sites/statesymbolsusa.org/files/\
primary-images/indianpaintbrushWYflower.jpg'''])

def displaying_menu():
    """ This function is used for displaying the main menu upon start
    and defines it throughout the program """
    print("\n")
    #Choice 1 for displaying all of the state's information
    print("1. Displaying all the U.S. States in Alphabetical order along, " +
    "with the Capital, State Population, and Flower.\n")
    #Choice 2 for searching for the state and displaying the individual
    #state's information along with the image to be opened up for viewing
    print("2. Searching for state and displaying appropriate Capital name, " +
          "State Population, and image of associated state flower.\n")
    #Choice 3 for displaying the bar graph of the 5 most populated states
    print("3. Providing a Bar graph of the top 5 populated States showing " +
          "their overall population.\n")
    #Choice 4 for updating the overall state's population and storing it for
    #next time use
    print("4. Updating the overall state population for a specific state.\n")
    #Choice 5 for exiting out of the program
    print("5. Exiting the program.\n")
    print("\n")
def bar_graphs_oftop_5_populated():
    """ This function is used to display a bar graph of the 5 populated states
    showing their overall population """
    displaying_data_of_states = []
    #This is used for displaying the populations of the five states
    #with the greatest population levels
    for i, populated_states in enumerate(state_information):
        #storing each state's information in list
        displaying_data_of_states.append([-int(state_information[i][2]),
                                               state_information[i][0]])
    #Sorting the states in list
    displaying_data_of_states.sort()
    #used for getting the state population of individual state
    population_state_list = []
    #Getting the sum of total lists of population needed for the states
    populated_states = []
    length_of_state_list = min(len(displaying_data_of_states),5)
    for i in range(length_of_state_list):
        population_state_list.append(-displaying_data_of_states[i][0])
        populated_states.append(displaying_data_of_states[i][1])
        #adding up each of the five states that consist of the highest population
        i = i + 1
    #Displaying the bar graph of the 5 most populated states
    plt.bar(populated_states, population_state_list)
    plt.show()
def displaying_state_information():
    """ Function used for displaying the individual's state information
    which includes the capital name, state population, and the flower """
    state_info_items = []
    #Used in displaying the individual's state information
    #First is State name, then capital, population, and then the state flower
    print(f"\n{'State' : <15} {'Capital': <15} {'Population': <15} {'Flower': <20}\n")
    for j, state_info_items in enumerate(state_information):
        #Displaying each state's information as mentioned above in tabular format
        print(f"{state_information[j][0] : <15} {state_information[j][1]: <15} " +
              f"{state_information[j][2]: <15} {state_information[j][3]: <20}")
        state_info_items.append(state_information)

def searching_for_state(state_name_entered):
    """ This function is designed to search the specific state name, and
    then print the required state information including the flower
    associated with the state, and other information as well """
    searching_for_specific_state = False
    #Displaying the header of each state to make sure when performing the
    #search for each state that it could be found much easier
    #print(f"\n{'State' : <20} {'Capital': <20} {'Population': <20} {'Flower': <25}\n")
    #if state_name_entered is True
    for k, searching_for_specific_state in enumerate(state_information):
        if (state_name_entered.lower()) == (state_information[k][0].lower()):
            print(f"\n{'State' : <15} {'Capital': <15} {'Population' : <15} {'Flower': <20}\n")
            flower_image_link = state_information[k][4].replace("",'')
            link_reply = requests.get(flower_image_link)
            state_flower_image = Image.open(BytesIO(link_reply.content))
            print(f"{state_information[k][0] : <15} {state_information[k][1]: <15} " +
                  f"{state_information[k][2]: <15} {state_information[k][3]: <20}")
            state_flower_image.show()
            searching_for_specific_state = True
    #returning the information for each associated state in the
    #state informatiion. (Consisted of State name, capital, population
    #and the flower name)
    return searching_for_specific_state

def updating_state_population(state_name, current_population):
    """ This function is designed to update the searched
    state's population and then return the updated population of
    state searched """
    #Setting searched state to false, as we have not begun
    #updating the searched state to update the population of
    #that state
    searched_state = False
    #Searching for the appropriate state
    for k, searched_state in enumerate(state_information):
        if (state_name.lower()) == (state_information[k][0].lower()):
            #Updating the current population of the searched state
            state_information[k][2] = current_population
            #Set the name of the state searched to True as we
            #have updated the population of it.
            searched_state = True
    #returning the searched state, and the updated population
    return searched_state

if __name__ == "__main__":
  # This is the main execution of the entirety of the program
  # If user chooses choice 1: Program will display the state's information
  # If user chooses choice 2: Searching for the appropriate state, and if it
  # does not exist program will provide a message saying so.
  # If user chooses choice 3: The bar graph of the top 5 most populated
  # states will be displayed.
  # If user chooses choice 4: Updates the state population provided that
  # accurate state name is inputted.
  # If user chooses choice 5: Program will terminate with a thank you
    #message and exit. """
    #Welcome message to be displayed for any user trying out the program
    print("\nHello user, Welcome to the State Capital and Flower List Program!")
    while 1:
        #Calling this function to display the overall
        #options menu.
        displaying_menu()
        #User will get the chance to enter an option between
        #1-5 here.
        user_input_choice = (input(("Enter a choice (1-5): ")))
        #If the user enters choice 1, this will be used to display
        #all of the individual states' information such as the
        #capital, the flower associated with each state, the
        #population currently associated with each state, and
        #the state itself.
        if user_input_choice[0] == '1':
            displaying_state_information()
        #This is choice 2 which is designed for entering the appropriate
        #state and along that the information of the state such as the
        #capital, population of the state, and loading the flower
        #associated for each state
        elif user_input_choice[0] == '2':
            entering_state = input("Enter state: ")
            making_sure_state_exists = searching_for_state(entering_state)
            if making_sure_state_exists is False:
                print(f"{entering_state} does not exist, please enter a valid state.")
        #This is choice 3 used to display the most populated five states
        #the bar graph populations of the five most populated states
        elif user_input_choice[0] == '3':
            #Put the bar graph function to be working
            bar_graphs_oftop_5_populated()
        #This is choice 4 used for entering the state name and population
        #of the state, and would update the population of the associated
        #state if and only if the state is a valid state
        elif user_input_choice[0] == '4':
            user_input_state = input('Enter State name: ')
            user_input_population = input('Enter the state population: ')
            #Checking to see if state entered is valid
            making_sure_state_exists = updating_state_population(user_input_state,
                                                                 user_input_population)
            if user_input_state is False:
                print(f"{user_input_state} is not a valid state, try again.")
        #This is choice 5, if the user wants to exit the program the user
        #can choose to do so.
        elif user_input_choice[0] == '5':
            print("Thank you for testing my program application, take care!")
            sys.exit()
        #if user enteres any other input besides 1-5, the following would be
        #displayed to the screen
        else:
            print("Not a Valid Input: Enter a value between the range 1-5.")
            
