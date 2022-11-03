#b_highscore.py

'''
title: high score tracker
author: kliment lo
date: november 1, 2022
'''
FILENAME = "c_highscore_rockpaperscissors"

# --- INPUTS --- #
def menu():
    '''
    User chooses the operation
    :return: (int)
    '''

    print("""
1. View Scores
2. Add New Score
3. Exit
    """)
    CHOICE = input("> ")
    if CHOICE.isnumeric():
        CHOICE = int(CHOICE)
    else:
        print("Please enter a number! ")
        return menu()
    if CHOICE > 0 and CHOICE < 4:
        return CHOICE
    else:
        print("Please enter a number in the menu! ")
        return menu()

def getFileRead():
    '''
    open the score file and create one if it doesn't exist
    :return: (obj)
    '''
    global FILENAME
    try:
        FILE = open(FILENAME, "x")
        START_SCORE = []
        for i in range(10):
            START_SCORE.append("AAA 0")
        START_SCORE_TEXT = ",".join(START_SCORE)
        FILE.write(START_SCORE_TEXT)
        FILE.close()
    except FileExistsError:
        pass
    FILE = open(FILENAME)
    return FILE

def getScore():
    '''
    get the player's score
    :return: (int)
    '''
    SCORE = input("Score: ")
    if SCORE.isnumeric():
        return int(SCORE)
    else:
        print("Please enter a number! ")
        return getScore()


def getName():
    '''
    asks user for their name
    :return: (str)
    '''
    NAME = input("Name: ")
    NAME = NAME.upper()
    if len(NAME) > 3:
        NAME = NAME[:3]
    return NAME
# --- PROCESSING --- #
def readFile(FILE_OBJ):
    '''
    Reading the contents of the file/
    :param FILE_OBJ: (obj)
    :return: (list)
    '''
    TEXT = FILE_OBJ.read()
    print(f" Text = what's on file: {TEXT}")
    FILE_OBJ.close()
    SCORE_ARRAY = TEXT.split(",")
    print(f"Text gets split: {SCORE_ARRAY} (makes it a list now)")
    return SCORE_ARRAY

def checkNewScore(SCORE, SCORE_ARRAY):
    '''
    tests whether the new scorse is a high score
    :param SCORE: (int)
    :param SCORE_ARRAY: (list)
    :return: (bool)
    '''
    SCORE_ARRAY_2D = []
    # Creates a 2d ARRAY with the scores set as integers
    for i in range(len(SCORE_ARRAY)):
        SCORE_ARRAY_2D.append(SCORE_ARRAY[i].split())
        SCORE_ARRAY_2D[-1][1] = int(SCORE_ARRAY_2D[-1][1])

    for i in range(len(SCORE_ARRAY_2D)):
        if SCORE >= SCORE_ARRAY_2D[i][1]:
            return True
    return False

def updateHighScore(SCORE, NAME, SCORE_ARRAY):
    '''
    updates score list with new score
    :param SCORE: (int)
    :param NAME: (str)
    :param SCORE_ARRAY: (list)
    :return: (list)
    '''
    SCORE_ARRAY_2D = []
    # Creates a 2d ARRAY with the scores set as integers
    for i in range(len(SCORE_ARRAY)):
        SCORE_ARRAY_2D.append(SCORE_ARRAY[i].split())
        SCORE_ARRAY_2D[-1][1] = int(SCORE_ARRAY_2D[-1][1])
    for i in range(len(SCORE_ARRAY)):
        if SCORE > SCORE_ARRAY_2D[i][1]:
            SCORE_ARRAY.insert(i, f"{NAME} {SCORE}")
            SCORE_ARRAY.pop()
            return SCORE_ARRAY

# --- OUTPUTS --- #
def viewScores(SCORES):
    '''
    display scores nicely
    :param SCORES: (list)
    :return: (none)
    '''
    print("High Scores")
    for i in range(len(SCORES)):
        print(f"{i+1}. {SCORES[i]}")

def writeFile(SCORE_ARRAY):
    '''
    writes the changes to the file
    :param SCORE_ARRAY: (list)
    :return:
    '''
    global FILENAME
    FILE = open(FILENAME, "w")
    SCORE_TEXT = ",".join(SCORE_ARRAY)
    FILE.write(SCORE_TEXT)
    FILE.close()
    print("Successfully saved High Score! ")


if __name__ == "__main__":
    FILENAME = "b_score.txt"
    FILE = getFileRead()
    SCORES = readFile(FILE)
    while True:
        CHOICE = menu()
        if CHOICE == 1:
            viewScores(SCORES)
        elif CHOICE == 2:
            SCORE = getScore()
            if checkNewScore(SCORE, SCORES):
                print("High Score! Congratulations! ")
                NAME = getName()
                SCORES = updateHighScore(SCORE, NAME, SCORES)
                writeFile(SCORES)
            else:
                print("Score is not high enough ... :(")
        elif CHOICE == 3:
            exit()