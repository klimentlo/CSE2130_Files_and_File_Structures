#g_large_mammal_population.py

'''
title:large mammal popu
author: kliment lo
date: november 22, 2022
'''

# --- INPUTS --- #
def openFileRead(FILENAME):
    return open(FILENAME)

def readCSV(FILE):
    '''
    extracts the contents of th efile into a 2D array
    :param FILE: (obj)
    :return: (list)(2d array)
    '''
    TEXT_LIST = FILE.readlines()
    FILE.close()
    print(TEXT_LIST)
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
    DATA = dataContent[1:]
    print(f"BALLS {DATA}")
    for i in range(len(DATA)):
        for j in range(3):
            DATA[i].pop(2)


    print(DATA)
# --- PROCESSING --- #



# --- OUTPUTS --- #


### --- MAIN PROGRAM --- ###

if __name__ == "__main__":
    #intro()
    dataContent = readCSV(openFileRead("01_CSE2130 - Elk_Island_NP_Grassland_Forest_Ungulate_Population_1906-2017_data.csv"))
    print(dataContent)
    bisonData = sortData("Bison")
    #elkData = sortData("Elk")
    #mooseData = sortData("Moose")
    #deerDara = sortData("Deer")
    #all


    #while True:
        #CHOICE = menu()
        #if CHOICE == 1:

        #elif CHOICE == 2:

        #else:
            #exit()