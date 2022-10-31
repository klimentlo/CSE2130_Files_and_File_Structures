#a_file_actions.py

'''
title: CRUD in files
author: kliment lo
date: october 31, 2022
'''

## Creating a file



if __name__ == "__main__":
    #Create a File
    FILENAME = "crud.txt"
    FILE = open(FILENAME, "w")
    #Close a File
    ##FILE.close()

    #Write to a file

    FILE.write("Hello World \n")

    FILE.close()
    FILE = open(FILENAME, "w")

    FILE.write("Happy Halloween! \n")

    FILE.close()

    ##Append to a File
    FILE = open(FILENAME, "a")
    FILE.write("Trick or Treat")
    FILE.close()

    ## Read a file
    FILE = open(FILENAME)
    TEXT = FILE.read()
    FILE.close()
    print(TEXT)

    ##Read line-by-line
    FILE = open(FILENAME)
    A_LIST = FILE.readlines()
    FILE.close()
    for i in range(len(A_LIST)):
        if i != len(A_LIST)-1:
            A_LIST[i] = A_LIST[i] [:-1] #gets rid of the \n thingy
    print(A_LIST)

### Delete a file
import os
os.remove(FILENAME)
