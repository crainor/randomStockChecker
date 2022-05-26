from cgi import test
from inspect import iscode
from setuptools import extension
from fileinput import filename
from itertools import count
import random
import datetime
from typing import Counter
import os

#A simple script to ensure a truly random choice when doing the daily random
# stock takes. A work in progress at the moment. Not all locations added
# and wont generate any "E" Locations as not implemented yet.

#C Reyner 2022

# Functions - CScott
#Small function that will add (1) on to the end to stop files being created with the same name.
def createFilePath(path):
    file, extension = os.path.splitext(path)
    counter = 1
    while os.path.exists(path):
        path = file + " (" + str(counter) + ") " + extension
        counter += 1
    
    return path

#Function to check if an input is either "Y" "N". 
def yesNoCheck(input):
    if input == "Y" or input == 'N' or input == "n"  or input == 'y':
        return True
    else:
        return False



#date n time
today = datetime.datetime.now()
fileName = "Random Stock Take - " + today.strftime("%d " ) + today.strftime("%b") + ".txt"
fileName = createFilePath(fileName)
#numLocations = input("How many locations would you like to check?")

while True:
    try:
        numLocations = int(input("How many locations would you like to check?"))
    except ValueError:
        print("Please enter a number")
        continue
    if numLocations < 0:
        print("Please enter a positive number")
        continue
    if numLocations > 20:
        print("There are only a maximum of 20 spots for a stock check")
    else:
        break
    

# Racking Locations

rackingArrayLoc = ["A1", "A2" , "A3", "A4", "A5", "A6", "A7", "A8", "A9",
                   "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B9",
                   "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9",
                   "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9",
                   "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9",
                   "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10", "G11",
                   "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11"]

rackingLetters = ["A", "B", "C", "D"]


                 
#Need to add rest of racking spots + letters (in a seperate array then use concancation to combine)

randomCheck= []
randomLetter = []
isCorrect = []

for x in range(numLocations):
    isCorrect.append("NULL")
    randomCheck.insert(x, random.choice(rackingArrayLoc))
    randomLetter.insert(x, random.choice(rackingLetters))

print(datetime.datetime.now())
print("This program will generate random locations in order to eliminate bias and ensure a 'Truly Random' choice is selected")
print("The Locations are:")


for i in range(numLocations):
    print(randomCheck[i] + "-" + randomLetter[i])


#isCorrect checks


print("Did the locations hold the correct stock? Please answer Y / N")



for i in range(numLocations):
    
    while True:
        isCorrect[i] = input(randomCheck[i] + "-" + randomLetter[i] + ":").upper()
       
        if yesNoCheck(isCorrect[i]) != True:
            print(isCorrect[i])
            print("\n ERROR Please enter Y or N \n")
            continue
        else:
            print("Thanks")
        break


#Print log file for digital records


f = open(fileName, "x")
for i in range(numLocations):
    f.write(randomCheck[i] + "-" + randomLetter[i]+ ": " + isCorrect[i] + "\n")
f.close()

print("The results have been saved to the directory.")
print("Press enter to exit.")
input()


