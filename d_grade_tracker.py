#d_grade_tracker.py

'''
title: grade tracker
author: kliment lo
date: november 3, 2022
'''

# --- VARIABLES --- #
FILENAME = "tracker.text"

# --- INPUTS --- #
def menu():
    '''
    User chooses the operation
    :return: (int)
    '''

    print("""
1. View Grades
2. Add Subject
3. Update Subject
4. Delete Subject
5. Calculate average

    """)
    CHOICE = input("> ")
    if CHOICE.isnumeric():
        CHOICE = int(CHOICE)
    else:
        print("Please enter a number! ")
        return menu()
    if CHOICE > 0 and CHOICE < 6:
        return CHOICE
    else:
        print("Please enter a number from the menu! ")
        return menu()

def getFileRead():
    '''
    open the score file and create one if it doesn't exist
    :return: (obj)
    '''
    global FILENAME
    try:
        FILE = open(FILENAME, "x") # try to make a file called {FILENAME} (should be a string)
        START_SCORE = []
        for i in range(10):
            START_SCORE.append("SUB 0 ") #SUB 0 gets appending into start_score 10 times
        START_SCORE_TEXT = ",".join(START_SCORE)  # removes all the commas
        FILE.write(START_SCORE_TEXT) # File then copies all the strings from "START_SCORE_TEXT"
        FILE.close() # Closes the file
    except FileExistsError: # if this file already exists
        pass #do nothing
    FILE = open(FILENAME) # opens up the file to be used in program
    return FILE # returns the file itself



# --- PROCESSING --- #
def readFile(FILE_OBJ):
    '''
    Reading the contents of the file
    :param FILE_OBJ: (obj)
    :return: (list)
    '''
    TEXT = FILE_OBJ.read() # Text = the contents on the file
    print(f" Text = what's on file: {TEXT}") # uncomment this to understand, you dummy
    FILE_OBJ.close() # closes file
    SCORE_ARRAY = TEXT.split(",") # makes everything with a comma its own index in a list
    print(f"Text gets split: {SCORE_ARRAY} (makes it a list now)")
    return SCORE_ARRAY


# --- OUTPUTS --- #
def viewGrades(GRADES):
    '''
    display scores nicely
    :param SCORES: (list)
    :return: (none)
    '''
    print("High Scores")
    for i in range(len(GRADES)): # if i is in the length of
        print(f"{i+1}. {GRADES[i]}") # prints it out nicely in a beautiful row



if __name__ == "__main__":
    FILE = getFileRead()
    GRADES = readFile(FILE)
    while True:
        CHOICE = menu()
        if CHOICE == 1:
            viewGrades(GRADES)
        if CHOICE == 2:
            addSubject()