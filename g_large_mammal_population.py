#g_large_mammal_population.py

'''
title: large mammal population
author: kliment lo
date: november 22, 2022
'''

FILENAME = "01_CSE2130 - Elk_Island_NP_Grassland_Forest_Ungulate_Population_1906-2017_data.csv"

# --- INPUTS --- #
def openFileRead(FILENAME):
   return open(FILENAME) # opens the file

def menu():
   '''
   its the menu
   :return:
   '''
   option = input("""
Please choose an option:
1. Search Population Growth
2. Add new year data
3. Display Data   
4. Exit

> """)
   if option.isnumeric(): #if input is number
       option = int(option)
       if option > 0 and option < 5:
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
   TEXT_LIST = FILE.readlines() # reads all the lines in the file
   FILE.close()
   for i in range(len(TEXT_LIST)):
       if TEXT_LIST[i][-1] == '\n': # if the last thing is \n
           TEXT_LIST[i] = TEXT_LIST[i][:-1] # exclude it

       TEXT_LIST[i] = TEXT_LIST[i].split(",") # whenever there is a comma, make it its own index

   for i in range(len(TEXT_LIST)):
       for j in range(len(TEXT_LIST[i])):
           if TEXT_LIST[i][j] == "": # if the thing is nothing
               TEXT_LIST[i][j] = "NA" # make it NA
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
   if animal != "area": # if the animal isn't area
       for i in range(len(dataContent)):
           usedData.append([dataContent[i][5],dataContent[i][1], dataContent[i][16]])# appends the animal, population year, and fall population estimate
       if animal == "All": # if they want all the data
           for i in range(len(dataContent)):
               returnData.append(usedData[i])  # keep everytihng
       else: # if they chose a specific animal
           for i in range(len(dataContent)):
               if usedData[i][0] == animal : #if the animal matches what the user inputted
                   returnData.append(usedData[i]) #return that data
   else: # if it wants to include the area of wehre the animal came from
       for i in range(len(dataContent)):  #include the area when appending it
           usedData.append([dataContent[i][0], dataContent[i][5], dataContent[i][1]]) # appends the area, animal, population year, and fall population estimate

       for j in range(len(dataContent)):
            returnData.append(usedData[j]) #appends everything, and it includes area
   return returnData

def getStartYear():
   '''
    gets the startyear
   :param NUMBER: (str)
   :return: (str)
   '''
   global dataContent
   year = input("Start year? ")
   if year.isnumeric(): # if its a number
       for i in range(len(dataContent)):
           if year == dataContent[i][1]: #if the year matches with any of the years on the datachart
               return year
   print("That year is not valid! ") # if not, redo
   return getStartYear()

def getEndYear(STARTYEAR):
   '''
    gets the endyear
   :param NUMBER: (str)
   :return: (str)
   '''
   global dataContent
   year = input("End year? ")
   if year.isnumeric(): # if its number
       for i in range(len(dataContent)):
           if year == dataContent[i][1]: # if theres any years  that match
               if year >= STARTYEAR: # if the end year is later then start year
                   return year
               else: # if the end year earlier than startyear
                   print("The end year must be later than the start year! ")
                   return getEndYear(STARTYEAR)
   print("That is not a valid year!")
   return getEndYear(STARTYEAR)

def getAnimal():
   '''
   gets what animal they want
   :return: (int)
   '''
   animal = input("""
Bison(1), Elk(2), Moose(3), Deer(4), or All(5)? """)
   try:
       animal = int(animal) # make it a integer
       if animal > 0 and animal < 6: # if its within 1-5
           return animal
       else:
           print("That is not one of the options")
           return getAnimal()
   except:
       print("That is not one of the options")
       return getAnimal()
# if user chooses option 2

def getArea():
    '''
    asks user what area the animal comes from
    :return: (int)
    '''
    area = input("North(1) or South(2)? ")
    try:
        area = int(area)
        if area > 0 and area < 3:
            if area == 1:
                area = "North"
            if area == 2:
                area = "South"
            return area
        else:
            print("That is not one of the options")
            return getArea()
    except TypeError:
        print("Please enter a number. ")
        return getArea()

def getAnimal2(): # this is used purely for the add new info
    '''
    asks what animal they would like to add
    :return:
    '''
    animal = input("Bison(1), Elk(2), Moose(3), Deer(4) ")
    try:
        animal = int(animal) 
        if animal > 0 and animal < 5:
            if animal == 1:
                animal = "Bison"
            if animal == 2:
                animal = "Elk"
            if animal == 3:
                animal = "Moose"
            if animal == 4:
                animal = "Deer"
            return animal
        else:
            print("That is not a valid number! ")
            return getAnimal2()
    except TypeError:
        print("Please input a number! ")
        return getAnimal2()

def getYear():
    '''
    asks the user for the year
    :return:
    '''
    year  = input("Year? ")
    if year.isnumeric():
        return year
    else:
        print("That is not a number! ")
        return getYear()

def getAmount():
    '''
    asks user the number of animals in that year
    :return:
    '''
    amount = input("Estimate Population Count? ")
    if amount.isnumeric():
        amount = int(amount)
        if amount > 0:
            return amount
        else:
            print("Please enter a positive number!")
            return getAmount()
    else:
        print("Please enter a valid year! ")
        return getAmount()

def addData():
    '''
    :return:
    '''
    global allDataAdd, dataContent

    area = getArea() # get the area
    animal = getAnimal2() # get the animal
    year = getYear() # get the year
    fileContent = dataContent # make "fileContent" equal all the data
    for i in range(len(allDataAdd)):
        if year == allDataAdd[i][2]: #checks if this year already exists
            if area == allDataAdd[i][0]: # checks if this area exists
                if animal == allDataAdd[i][1]: # checks if this animal in this year and area exists
                    print("""That data already exists! Try again with a new time period. 
""")
                    return addData() #request all the stuff again
    #if theres no duplicate
    amount = str(getAmount()) #get the amount of animals in that year
    dataSet = [area, year, "NA", "NA", "NA", animal, "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", "NA", amount, "NA", "NA"] # combine all the informatio nand make it into an array
    fileContent.append(dataSet) # append it into all the data
    return fileContent #return it

def writeFile(DATA):
    '''
    updates the file
    :param data: list
    :return:
    '''
    global FILENAME
    FILE = open(FILENAME, "w")
    DATA_TEXT = ""
    for i in range(len(DATA)):
        DATA_TEXT = DATA_TEXT + ",".join(DATA[i]) + "\n" # joins eat array in the 2d array, line breaks it, and then replaces it's current information
    FILE.write(DATA_TEXT) # write this new information
    FILE.close() # close


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
   elif animal == 5: # if all is chosen, use all animals data
       animal = ["Bison", "Elk", "Moose", "Deer"]
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
   if animal == ["Bison", "Elk", "Moose", "Deer"]:
       bisonStartAverage = 0
       elkStartAverage = 0
       mooseStartAverage = 0
       deerStartAverage = 0
       bisonEndAverage = 0
       elkEndAverage = 0
       mooseEndAverage = 0
       deerEndAverage = 0
       for i in range(len(calculateData)):
           if calculateData[i][1] == startYear: # if the years match as what the user inputted
               if calculateData[i][0] == "Bison": # if the animal matches with the bison
                   bisonStartAverage = bisonStartAverage + int(calculateData[i][2]) # add all the start years of bison
               if calculateData[i][0] == "Elk": # if the animal matches with the elk
                   elkStartAverage = elkStartAverage + int(calculateData[i][2]) # add all the start years of elk
               if calculateData[i][0] == "Moose": # if the animal matches with the moose
                   mooseStartAverage = mooseStartAverage + int(calculateData[i][2]) # add all the start years of moose
               if calculateData[i][0] == "Deer": # if the animal matches with the deer
                   deerStartAverage = deerStartAverage + int(calculateData[i][2]) # add all the start years of deer

           if calculateData[i][1] == endYear: # gets the population of the animal s that corespond with what year the user inputted
               if calculateData[i][0] == "Bison": # same thing, but for end year
                   bisonEndAverage = bisonEndAverage + int(calculateData[i][2])
               if calculateData[i][0] == "Elk":
                   elkEndAverage = elkEndAverage + int(calculateData[i][2])
               if calculateData[i][0] == "Moose":
                   mooseEndAverage = mooseEndAverage + int(calculateData[i][2])
               if calculateData[i][0] == "Deer":
                   deerEndAverage = deerEndAverage + int(calculateData[i][2])

   startYear = int(startYear)  # makes it a integer so we can calculate with it
   endYear = int(endYear)  # ^^
   yearDifference = endYear - startYear # get year differnce

   if yearDifference == 0: # if its a 0
       yearDifference = 1 # make it one to avoid error

   average = (averageEnd - averageStart) / (yearDifference) # calculate the average
   try:
       average = int(average) # try to convert it to integer
   except: # if it doesn't work
       average = round(average, 2) # round it to decimal of 2

   if animal == ["Bison", "Elk", "Moose", "Deer"]: # if all the animals are chosen
       averageAll = []
       averageAll.append((bisonEndAverage - bisonStartAverage) / (yearDifference)) # append the bison average to this thing
       averageAll.append((elkEndAverage - elkStartAverage) / (yearDifference))  # append the elk average to this thing
       averageAll.append((mooseEndAverage - mooseStartAverage) / (yearDifference))  # append the moose average to this thing
       averageAll.append((deerEndAverage - deerStartAverage) / (yearDifference)) # append the deer average to this thing

       for i in range(len(animal)):
           print(f"""The growth rate {animal[i]} between {startYear} and {endYear} is {averageAll[i]}/year. """)
       print(f"""
The total growth rate of all 4 species between {startYear} and {endYear} is {average}/year. """)

   else: # if its just a single animal
       print(f"""
The growth rate of {animal} between {startYear} and {endYear} is {average} {animal}/year. """)



# --- OUTPUTS --- #
def intro():
   '''
   introduction/instructions to program
   :return:
   '''
   print("""
Welcome to the Elk Island National Park Large Mammal population database! """)

def displayData(startYear, endYear, animal):
    '''
    displays the data out so the user can see it
    :param startYear: (str)
    :param endYear: (str)
    :param animal: (str)
    :return:
    '''
    global dataContent
    display = [["Area of park","Population year","Survey Year","Survey Month","Survey Day","Species name","Unknown age and sex count","Adult male count","Adult female count","Adult unknown count","Yearling count","Calf count","Survey total","Sightability correction factor","Additional captive count","Animals removed prior to survey"",Fall population estimate","Survey comment","Estimate method"]]
    startYear = str(startYear) # make sure its a string
    endYear = str(endYear) # make sure its a string

    for i in range(len(dataContent)):
        if animal == dataContent[i][5]: # if the animal and the animal the user inputted match
            if dataContent[i][1] >= startYear and dataContent[i][1] <= endYear: # if they are within the start and end year
                display.append(dataContent[i]) # append that data into a new list

    for i in range(len(display)):
        display[i] = "| " + " | ".join(display[i]) + " |" # join the each list in the 2 d list with itself, and inserts a | to seperate the data
        print(display[i]) # print it out
    returnhome = input(""" 
Press any key to return to menu. """) #restricts the menu from popping up immedietly

### --- MAIN PROGRAM --- ###

if __name__ == "__main__":
   intro() # intro
   while True:
       dataContent = readCSV(openFileRead(FILENAME)) # read the file content to only what we want
       # everything here only extacts the animal name, population year, and estimated population count
       bisonData = sortData("Bison") # isolate it to only bison data
       elkData = sortData("Elk") # only get elk data
       mooseData = sortData("Moose") # only get moose data
       deerData = sortData("Deer") # only get deer data
       allData = sortData("All") # get all species' data
       # different \/
       allDataAdd = sortData("area") # it gets all the species' data, but also includes the area of which it came from (north or south)
       choice = menu() # get choice
       if choice == 1: # if they chose to calculate average
           startYear = getStartYear() # get start year
           endYear = getEndYear(startYear) # get the end year
           animal = getAnimal() # get the animal
           growthRate = calculateGrowthRate(startYear, endYear, animal) # calculate the growthrate
       elif choice == 2: # if they want to add data
            updatedData = addData() # calculate all of that stuff
            writeFile(updatedData) # update the file with the new information
       elif choice == 3: # if they want to display specific information
           startYear = getStartYear() # get the start year
           endYear = getEndYear(startYear) # get the end year
           animal = getAnimal2() # get the animal (the straight up string)
           displayData(startYear, endYear, animal) # displays it out nicely
       elif choice == 4: # if they want to exit
           exit() #exit


