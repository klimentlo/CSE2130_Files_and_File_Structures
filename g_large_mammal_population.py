#g_large_mammal_population.py

'''
title: large mammal population
author: kliment lo
date: november 22, 2022
'''

# --- INPUTS --- #
def openFileRead(FILENAME):
    return open(FILENAME)

def menu():
    '''
    its the menu
    :return:
    '''
    try:
        option = int(input("""Please choose an option: 
1. Search Population Growth 
2. Add new year data    
3. Exit

> """))
        if option > 0 and option < 4:
            return int(option)
        else:
            print("That is not one of the options! ")
            menu()
    except:
        print("That is not a number! ")
        menu()


def readCSV(FILE):
    '''
    extracts the contents of th efile into a 2D array
    :param FILE: (obj)
    :return: (list)(2d array)
    '''
    TEXT_LIST = FILE.readlines()
    FILE.close()
    for i in range(len(TEXT_LIST)):
        if TEXT_LIST[i][-1] == '\n':
            TEXT_LIST[i] = TEXT_LIST[i][:-1]
        TEXT_LIST[i] = TEXT_LIST[i].split(",")
    return TEXT_LIST

def sortData(ANIMAL):
    '''
    sorts out the data based on the anima;
    :param ANIMAL: (str)
    :return: (2d array)
    '''
    global dataContent
    usedData = []
    returnData = []
    for i in range(len(dataContent)):
        usedData.append([dataContent[i][5],dataContent[i][1], dataContent[i][14]])

    for i in range(len(dataContent)):
        if usedData[i][0] == ANIMAL:
            returnData.append(usedData[i])
    return returnData

# --- PROCESSING --- #

def calculateAverage(STARTYEAR, ENDYEAR, ANIMAL):
    '''
    calculates the total growth rate of the animal
    :param STARTYEAR: (int)
    :param ENDYEAR: (int)
    :param ANIMAL: (int)
    :return:
    '''
    global bisonData, elkData, mooseData, deerData
    if ANIMAL == 1:
        print(bisonData)
    elif ANIMAL == 2:
        print(elkData)
    elif ANIMAL == 3:
        print(mooseData)
    elif ANIMAL == 4:
        print(deerData)

# --- OUTPUTS --- #
def intro():
    '''
    introduction/instructions to program
    :return:
    '''
    print("""
Welcome to the Elk Island National Park Large Mammal population database! """)



### --- MAIN PROGRAM --- ###

if __name__ == "__main__":
    intro()
    dataContent = readCSV(openFileRead("01_CSE2130 - Elk_Island_NP_Grassland_Forest_Ungulate_Population_1906-2017_data.csv"))
    bisonData = sortData("Bison")
    elkData = sortData("Elk")
    mooseData = sortData("Moose")
    deerData = sortData("Deer")
    #all

    while True:
        choice = menu()
        if choice == 1:
            startYear = input("Start year? ")
            endYear = input("End year? ")
            animal = int(input("Bison (1), Elk(2), Moose(3), Deer(4), or All(5)? "))
            calculateAverage(startYear, endYear, animal)
        elif choice == 2:
            pass
        elif choice == 3:
            exit()