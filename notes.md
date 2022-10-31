# CSE2130_Files_and_File_Structures

Files are used in programs to store data. That data is often processed by the program to create information usable by the program or user. The main advantage to incorporating files into a program is data persistence, which means the data is available beyond the running of the program.

Files can be used to store default setting and startup instructions, which can even be edited by an external editor, they can also be used to store information created by the program for future use.

Another major advantage to implementing files is that those files can have structures that ensure data integrity. data integrity is the degree of reliability of the data.

## CRUD in Text Files
### Crate Text Files
Creating a text file in python will also grant file write privileges. 
```python
FILE = open("filename.ext", "x")
```
The function above creates a file with the given file name, opens it, and allows write access. However, if there is a file that already exists with that name, it will throw a FileExistsError and stop the python interpreter. An alternative is to use write plus setting.
```python
FILE = open("filename.ext", "w")
```
The above methods will overwrite any information with new information .

NOTE: The program will look for the file relative to its location from the program file. (Most likely, this will be the project's root/main folder.) 

If information needs to be added to the end of the text files, use the "a" setting (for append).
```python
FILE = open("filename.ext", "a")
```
### Close a File
While closing a file is not mandatory, the file will remain in computer memory until it is closed. Therefore, to reduce potential memory leak, files should be closed immediately after they are read or written to.

## Write to a File
Writing to a text file uses the ```.write(STRING)``` function. It can only write strings to the file.

```python
FILE = open("hello-world.txt", "w")
FILE.write("hello world")
FILE.close()
```

### Reading contents of a text file
A file that is open i n write mode cannot be read and vice versa. To open a file in read mode; use the following:
```python
FILE = open("filename.ext")
TEXT = FILE.read()
FILE.close()
print(TEXT)
```

### Reading Files Line-By-Line
When preserving information in each row of a spreadsheet file, reading the file line by line ensures that the overall structure of the tables is maintained.
```python
FILE = open("filename.ext") # we don't need the extension thingy, cause we're just opening it to read it
A_LIST = FILE.readlines()
FILE.close()
print(A_LIST)
```
NOTE: Formatting characters such as \n will be visible in strings created from readlines(). Therefore, the data ofter requires clean-up of unanticipated characters. 

## Updating Files
Updating a file requires reading the file to extract the text, then making changes to the text and then overwriting the file with the new text.
```python
FILE = open("filename.ext", "w")
TEXT = FILE.read()
## Processing the data
FILE.write(TEXT)
FILE.close()
```

###Deleting a File
To delete content within a file, overwrite the content with a blank string
```python
FILE = open("filename.ext", "w")
FILE.write("")
FILE.close()
```
To delete a file, python requires access to the operating system to ensure appropriate file manage permissions.
```python
import os
os.remove("filename.ext")
```