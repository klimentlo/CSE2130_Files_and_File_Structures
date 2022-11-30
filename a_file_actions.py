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

    FILE.write("Hello World?")
    FILE.close()

    FILE = open(FILENAME)
    READ = FILE.read()
    print(f"FILE.READ: {READ}")

    FILE = open(FILENAME, "w")
    FILE.write("Happy Halloween!")

    FILE.close()

    ##Append to a File
    FILE = open(FILENAME, "a")
    FILE.write("Trick or Treat, hello")
    FILE.close()

    ## Read a file
    FILE = open(FILENAME)
    TEXT = FILE.read()
    FILE.close()
    print(f"This is FILE.read: {TEXT}")

    ##Read line-by-line
    FILE = open(FILENAME)
    A_LIST = FILE.readlines()
    print(f"This is readlines with getting rid of /n {A_LIST} hi")
    FILE.close()
    for i in range(len(A_LIST)):
        if i != len(A_LIST)-1:
            A_LIST[i] = A_LIST[i] [:-1] #gets rid of the \n thingy

### Delete a file
import os
os.remove(FILENAME)
