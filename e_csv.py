#e_csv.py
'''
Title: Working with CSV Files
Author: Kliment Lo
Date: November 16, 2022
'''


import csv
FILE = open("e_board_games.csv", newline="")
READER = csv.reader(FILE)

for row in READER:
    print(row)
FILE.close()

NEW_GAME = ["Final Girl", "Fight horror movie monsters to survive", "---", "---", "---"]

FILE = open("e_board_games.csv", "a", newline="")
WRITER = csv.writer(FILE)
WRITER.writerow(NEW_GAME)
FILE.close()

FILE = open("e_board_games.csv", newline="")
READER = csv.reader(FILE)

for row in READER:
    print(row)

FILE.seek(1)
for row in READER:
    print(", ".join(row))

FILE.close()