#testing.py

'''
title: testing
author: kliment
date: november 7, 2022
'''
# --- VARIABLES --- #
FILENAME = "d_grades.txt"

# --- FUNCTIONS --- #

# -- INPUTS -- #
def menu():
    '''
    User selects the operation
    :return: CHOICE (int)
    '''
    print("""
1. View Grades
2. Add Subject
6. Save and Exit
""")
    CHOICE = input("> ")
    return int(CHOICE)

def askSubject():
    '''
    asks for the subject
    :return:
    '''
    return  input("Subject: ").capitalize()

def askGrade():
    '''
    Asks the user for the grade to add
    :return:
    '''
    return float(input("Grade: "))
# -- PROCESSING -- #

def openFileRead():
    '''
    Opens a file as read only
    :return: FILE
    '''
    global FILENAME
    try:
        FILE = open(FILENAME)
        return FILE
    except FileNotFoundError:
        FILE = open(FILENAME, "x")
        FILE.write("")
        FILE.close()
        FILE = open(FILENAME)
        return FILE

def openFileWrite():
    '''
    opens file as write
    :return: (obj)
    '''
    global FILENAME
    FILE = open(FILENAME, "w") # opens file in write plus
    return FILE

def getFileContent(FILE):
    '''
    reads the file contents and processes it into a 2D Array
    :param FILE: (obj)
    :return: (2D array)
    '''
    '''
["Math 87\n"]
["Science 43\n"]
["CompSci 92\n"]
    '''
    ROWS = FILE.readlines()
    print(ROWS)
    for i in range(len(ROWS)): # 0, 1, 2
        if i < len(ROWS) - 1 : #
            ROWS[i] = ROWS [i][:-1] # everything except for the last letter (which is \n) (cleans it up)
        # ["Math 87"], ["Science 43"] ["CompSci 92"]
        ROWS [i] = ROWS[i].split() # splits it, so its
        # [[Math, 87], [Science, 43], [CompSci, 92]]
        ROWS[i][1] = float(ROWS[i][1]) # makes it a float
    FILE.close() # closes the file
    return ROWS

# -- OUTPUTS -- #

def writeGrades(FILE, GRADES):
    '''
    saves chnges to the file
    :param FILE: (object)
    :param GRADES: (list)
    :return: (none)
    '''
    for i in range(len(GRADES)):
        GRADES[i][1] = str(GRADES[i][1]) # grabs the numerical grade and makes it a string
        # [("Math", "87"), ("Science", "43"), ("CompSci", "92")]
        GRADES[i] = " ".join(GRADES[i]) # replaces that specific 2D array, joins them together, creating a 1D array
        # ["Math 87", "Science 43", "CompSci 92"]
    TEXT = "\n".join(GRADES) # makes it one single string
    # "Math 87\nScience 43\nCompSci 92"
    FILE.write(TEXT) # replaces the entire file with this newly made version
    FILE.close() # closes the file

def viewGrades(GRADES):
    '''
    displays the grades nicely
    :return: (array)
    '''
    for GRADE in GRADES: #
        print(f" {GRADE[0]} {GRADE[1]}")


if __name__ == "__main__":
    FILE = openFileRead()
    GRADES = getFileContent(FILE)
    while True:
        CHOICE = menu()
        if CHOICE == 1:
            viewGrades(GRADES)
        if CHOICE == 2:
            SUBJECT = askSubject()
            GRADE = askGrade()
            GRADES.append([SUBJECT, GRADE])
        if CHOICE == 6:
            FILE = openFileWrite() # opens file as write plus (whatever you write, it overrides what's on the file)
            writeGrades(FILE, GRADES) # inputs the grades into the actual file
            print("Goodbye! :) ")
            exit()
