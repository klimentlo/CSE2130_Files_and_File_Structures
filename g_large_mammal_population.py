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
    option = input("""
Please choose an option: 
1. Search Population Growth 
2. Add new year data    
3. Exit

> """)
    if option.isnumeric():
        option = int(option)
        if option > 0 and option < 4:
            return option
        else:
            print("That is not one of the options! ")
            return menu()
    else:
        print("That is not a number! ")
        return menu()


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

def sortData(animal):
    '''
    sorts out the data based on the anima;
    :param animal : (str)
    :return: (2d array)
    '''
    global dataContent
    usedData = []
    returnData = []
    for i in range(len(dataContent)):
        usedData.append([dataContent[i][5],dataContent[i][1], dataContent[i][16]])# appends the animal, population year, and fall population estimate

    if animal == "All":
        for i in range(len(dataContent)):
            returnData.append(usedData[i])
    for i in range(len(dataContent)):
        if usedData[i][0] == animal : #
            returnData.append(usedData[i])
    return returnData

def getStartYear():
    '''

    :param NUMBER: (str)
    :return:
    '''
    global dataContent
    year = input("Start year? ")
    if year.isnumeric():
        for i in range(len(dataContent)):
            if year == dataContent[i][1]:
                return year
    print("That year is not valid! ")
    return getStartYear()

def getEndYear(STARTYEAR):
    '''

    :param NUMBER: (str)
    :return:
    '''
    global dataContent
    year = input("End year? ")
    if year.isnumeric():
        for i in range(len(dataContent)):
            if year == dataContent[i][1]:
                if year >= STARTYEAR:
                    return year
                else:
                    print("That is not a valid year! ")
                    return getEndYear(STARTYEAR)
    print("That is not a valid year!")
    return getEndYear(STARTYEAR)

def getanimal ():
    '''
    gets what animal they want
    :return:
    '''
    animal = input("""
Bison (1), Elk(2), Moose(3), Deer(4), or All(5)? """)
    try:
        animal = int(animal)
        if animal > 0 and animal < 6:
            return animal
        else:
            print("That is not one of the options")
            return getanimal()
    except:
        print("That is not one of the options")
        return getanimal()

# --- PROCESSING --- #

def calculateGrowthRate(startYear, endYear, animal ):
    '''
    calculates the total growth rate of the animal
    :param STARTYEAR: (str)
    :param ENDYEAR: (str)
    :param animal : (int)
    :return:
    '''
    global bisonData, elkData, mooseData, deerData, allData

    if animal == 1: #if bison was chosen, use bison data
        animal = "Bison"
        calculateData = bisonData
    elif animal == 2: #if elk was chosen, use bison data
        animal = "Elk"
        calculateData = elkData
    elif animal == 3: #if moose was chosen, use bison data
        animal = "Moose"
        calculateData = mooseData
    elif animal == 4: #if deer was chosen, use bison data
        animal = "Deer"
        calculateData = deerData
    elif animal == 5: # if all is chosen, use all animal s data
        calculateData = allData

    usedData = []
    for i in range(len(calculateData)):
        if calculateData[i][1] == startYear or calculateData[i][1] == endYear: # gets the population of the animal s that corespond with what year the user inputted
            usedData.append([calculateData[i][1],calculateData[i][2]]) # appends it as a list to be used for calculating average
    averageEnd = 0
    averageStart = 0
    for i in range(len(usedData)):
        if usedData[i][1] == "NA": # if the population is NA, make it a 0
            return print(f"There is insufficient data in year {usedData[i][0]}")

        if usedData[i][0] == endYear:
            averageEnd = averageEnd + int(usedData[i][1]) # adds all the populations together

        if usedData[i][0] == startYear:
            averageStart = averageStart + int(usedData[i][1])  # adds all the populations together

    startYear = int(startYear)  # makes it a integer so we can calculate with it
    endYear = int(endYear)  # ^^

    yearDifference = endYear - startYear
    if yearDifference == 0:
        yearDifference = 1

    average = (averageEnd - averageStart) / (yearDifference)
    try:
        average = int(average)
    except:
        average = round(average, 2)

    if average > 0:
        sign = "+"
    else:
        sign = ""

    if animal == 5:
        print(f"""
The growth rate of all 5 species between {startYear} and {endYear} is {sign}{average}/year. """)
    else:
        print(f"""
The growth rate of {animal} between {startYear} and {endYear} is {average} {sign}{animal}/year. """)








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
    allData = sortData("All")

    while True:
        choice = menu()
        if choice == 1:
            startYear = getStartYear()
            endYear = getEndYear(startYear)
            animal = getanimal()
            growthRate = calculateGrowthRate(startYear, endYear, animal)
        elif choice == 2:
            pass
        elif choice == 3:
            exit()