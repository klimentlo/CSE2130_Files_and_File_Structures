# d_board_games.py

'''
Title: Board Game Collection
Author:
Date:
'''
# --- VARIABLES --- #
FILENAME = "d_board_games.txt"


# --- INPUTS --- #
def menu():
    """Displays a menu of choices for the user to select

    Returns:
        CHOICE (int)
    """
    print("""
What would you like to do?
1. View Collection
2. Add a Game
3. Remove a Game
4. Check Size of the Collection
5. Check Average Playtime of the Collection
6. Check games with # players
7. Check games that start with \" \"
8. Check games above or below a certain difficulty
9. Save and Exit
    """)
    CHOICE = input("> ")
    return int(CHOICE)


def readFile():
    """Read the data from the file that will be used for the rest of the practice and clean-up.

    Returns:
        DATA_2D (list)
    """
    global FILENAME
    try:
        FILE = open(FILENAME, "x")
        FILE.write("")
        FILE.close()
    except FileExistsError:
        FILE = open(FILENAME)
        DATA = FILE.readlines()
        FILE.close()
        print("hi")
    print(DATA)
    DATA_2D = []
    for i in range(len(DATA)):
        DATA_2D.append(DATA[i].split(","))
        print(DATA_2D[i][-1])
        print(DATA_2D[i][-1][:-1])
        DATA_2D[i][-1] = DATA_2D[i][-1][:-1]  # removes the "\n" character from the end of the last entry of every line
    print(DATA_2D)
    return DATA_2D


# --- PROCESSING --- #
def fillData(DATA):
    """Ensures each line in the file has the same number of entries
    Args:
        DATA (list): A 2D Array of all of our Data
    Returns:
        DATA (list): Updated version of DATA
    """
    print("Your collection entries need to be normalized")
    for i in range(len(DATA)):
        while len(DATA[i]) > 5:
            DATA[i].pop(-1)
        while len(DATA[i]) < 5:
            DATA[i].append("N/A ")
        for j in range(len(DATA[i])):
            if DATA[i][j] == "" or DATA[i][j] == "---":
                DATA[i][j] = "N/A "


def normalizeData(DATA):
    """Converts the data to a standardized format for strings, ints, and floats
    Args:
        DATA (list):
    Returns:
        DATA (list)
    """
    print("Your collection values need to be normalized")
    # [[
    for i in range(len(DATA)-1): # runs 29 times
        DATA[i+1][0] = DATA[i+1][0].lower()
        DATA[i+1][0] = DATA[i+1][0].title()
        if DATA[i][0][-1:]!= ".":
            DATA[i][0] = DATA[i][0] + "."
        try:
            DATA[i+1][1] = str(DATA[i+1][1])
            DATA[i+1][2] = float(DATA[i+1][2])
            DATA[i+1][3] = int(DATA[i+1][3])
            DATA[+1][4] = int(DATA[i+1][4])
        except ValueError:
            pass
    print(DATA)
    return DATA


def addGame(DATA):
    """Adds a game to the Collection
    Args:
        DATA (list)
    """
    print("This function is under construction")
    GAME = str(input("Board game: "))
    DESCRIPTION = str(input("Description: "))
    DIFFICULTY = float(input("Difficulty: "))
    PLAYERS = int(input("Number of players: "))
    TIME = int(input("Time required to complete: "))
    DATA.append([GAME, DESCRIPTION, DIFFICULTY, PLAYERS, TIME])


def removeGame(DATA):
    """Removes a game from the collection

    Args:
        DATA (list)
    """
    LENG = len(DATA)
    REMOVE = input("Which game would you like to remove? ").title()
    for i in range(len(DATA)):
        if REMOVE == DATA[i][0]:
            DATA.pop(i)
            print("it exists!")
    NEW_LENG = len(DATA)
    if NEW_LENG == LENG: # checks if something got popped off or not
        print("That game is not on the list! ")
        removeGame(DATA)


def getPlayers(DATA):
    """Tells you how many games of a certain player count are within the collection

    Args:
        DATA (list)
    """
    print("This function is under construction")


def getBoardNum(DATA):
    """Tells you how many board games are in the collection

    Args:
        DATA (list)

    Returns:
        LINES (int)
    """
    print("This function is under construction")


def getAverageTime(DATA):
    """Tells you the average playtime of games in the collection

    Args:
        DATA (list)
    """
    print("This function is under construction")


def getNameRange(DATA):
    """Tells you how many games start with a certain letter

    Args:
        DATA (list)
    """
    print("This function is under construction")


def getDifficulty(DATA):
    """Tells you how many games there are above or below the selected difficulty level

    Args:
        DATA (list)
    """
    print("This function is under construction")


# --- OUTPUTS --- #
def intro():
    """Simple message display
    """
    print("Welcome to your Board Game Collection!\n")


def viewData(DATA):
    """Prints out the data in a visually pleasing way

    Args:
        DATA (list): A 2D Array of all of our Data
    """
    for i in range(len(DATA)):
        for j in range(len(DATA[i])):
            if DATA[i][j] != str(DATA[i][j]):
                DATA[i][j] = str(DATA[i][j])
        TEXT = ", ".join(DATA[i])
        print(TEXT)


def writeFile(DATA):
    """Writes the changes to the file
    Args:
        DATA (list)
    """
    global FILENAME
    FILE = open(FILENAME, "w")
    DATA_TEXT = ""
    for i in range(len(DATA)):
        DATA_TEXT = DATA_TEXT + ",".join(DATA[i]) + "\n"
    FILE.write(DATA_TEXT)
    FILE.close()
    print("Successfully saved Board Game Collection!")


if __name__ == "__main__":
    DATA = readFile()
    print(DATA)
    fillData(DATA)
    normalizeData(DATA)
    intro()
    while True:
        CHOICE = menu()
        if CHOICE == 1:  # View Collection
            viewData(DATA)
        elif CHOICE == 2:  # Add a Game
            addGame(DATA)
            normalizeData(DATA)
        elif CHOICE == 3:  # Remove a Game
            removeGame(DATA)
        elif CHOICE == 4:  # Check Size of the Collection
            getBoardNum(DATA)
        elif CHOICE == 5:  # Check Average Playtime of the Collection
            getAverageTime(DATA)
        elif CHOICE == 6:  # Check games with # Players
            getPlayers(DATA)
        elif CHOICE == 7:  # Check games that start with the given character
            getNameRange(DATA)
        elif CHOICE == 8:  # Check games above or below a certain difficulty
            getDifficulty(DATA)
        elif CHOICE == 9:  # Save and Exit
            writeFile(DATA)
            print("Thank you, goodbye!")
            exit()