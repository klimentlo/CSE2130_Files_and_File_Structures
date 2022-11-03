#c_highscore_rockpaperscissors.py

'''
title: rockpaperscissors high score
author: kliment lo
date: november 2
'''
from b_highscore import getFileRead, getScore, getName, readFile, viewScores, checkNewScore, updateHighScore, writeFile


from random import randrange
# --- INPUTS --- #

def checkInt(NUMBER):
    '''
    verifies if the number is an integer
    :param NUMBER: (str)
    :return: (int)
    '''
    if NUMBER.isnumeric():
        return int(NUMBER)
    else:
        print("That is not a number!")
        NEW_NUM = input("Please enter a valid number! ")
        return checkInt(NEW_NUM)

def chooseWeapon():
    """
    Prints a selection of weapons for the user to select
    :return: (int) chosen weapon
    """
    print("""
1. Rock
2. Lizard
3. Spock    
4. Scissors
5. Paper
""")
    WEAPON = input("> ")
    WEAPON = checkInt(WEAPON)
    if WEAPON > 0 and WEAPON < 6:
        return WEAPON
    else:
        print("Please choose a valid option from the list! ")
        return chooseWeapon()

def askContinue():
    '''
    asks if user would want to continue
    :return: (none)
    '''
    ANSWER = input("Would you like to continue playing? (y/n) ")
    if ANSWER == "Y" or ANSWER == "y" or ANSWER == "":
        return
    elif ANSWER == "N" or ANSWER == "n":
        exit()


# --- PROCESSING --- #

def getWinner(PLAYER, COMPUTER, WEAPONS):
    '''
    determines who the winner is
    :param PLAYER: (int) player weapon
    :param COMPUTER: (int) computer weapon
    :return: (int) Winner (0= tie, 1 = player, 2 = computer)
    '''
    global SCORE
    WEAPONS = ("Rock", "Lizard", "Spock", "Scissors", "Paper")
    if PLAYER == COMPUTER:
        return 0
    elif WEAPONS[COMPUTER] == WEAPONS[PLAYER - 1] or WEAPONS[COMPUTER] == WEAPONS[COMPUTER - 3]:
        return 2
    else:
        SCORE += 1
        return 1




# --- OUTPUTS --- #
def computerWeapon():
    '''
    computer randomly chooses a weapon
    :return:
    '''
    return randrange(5)

def displayWinner(WINNER):
    '''
    Displays the winner of the round
    :param WINNER:  (int) winner
    :return: (none)
    '''
    global SCORE
    global SCORES
    if WINNER == 0:
        print("You and the computer tied! ")
    elif WINNER == 1:
        print("You win! ")
        print(f"Current score: {SCORE}")
    elif WINNER == 2:
        print ("You lose... ")
        if checkNewScore(SCORE, SCORES):
            print("High Score! Congratulations! ")
            NAME = getName()
            SCORES = updateHighScore(SCORE, NAME, SCORES)
            writeFile(SCORES)
            viewScores(SCORES)



# --- MAIN PROGRAM --- #
if __name__ == "__main__":
    FILENAME = "c_highscore_rockpaperscissors.txt"
    SCORE = 0
    FILE = getFileRead()
    SCORES = readFile(FILE)

    while True:
        WEAPONS = ("Rock", "Lizard", "Spock", "Scissors", "Paper")
        USER = chooseWeapon()
        COMP = computerWeapon()
        WINNER = getWinner(USER, COMP, WEAPONS)
        displayWinner(WINNER)
