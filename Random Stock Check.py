import random
import datetime

#A simple script to ensure a truly random choice when doing the daily random
# stock takes. A work in progress at the moment. Not all locations added
# and wont generate any "E" Locations as not implemented yet.

#C Reyner 2022

#date n time
today = datetime.datetime.now()
fileName = "Random Stock Take - " + today.strftime("%d " ) + today.strftime("%b") + ".txt"


# Racking Locations

rackingArrayLoc = ["A1", "A2" , "A3", "A4", "A5", "A6", "A7", "A8", "A9",
                   "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B9",
                   "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9",
                   "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9",
                   "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9",
                   "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10", "G11",
                   "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11"]

rackingLetters = ["A", "B", "C", "D"]

#isCorrect checks - Variables to hold Y/N chars

isCorrect1  = ("")
isCorrect2  = ("")
isCorrect3  = ("")
isCorrect4  = ("")
isCorrect5  = ("")
isCorrect6  = ("")
isCorrect7  = ("")
isCorrect8  = ("")
isCorrect9  = ("")
isCorrect10  = ("")
                 
#Need to add rest of racking spots + letters (in a seperate array then use concancation to combine)

randomCheck1 = random.choice(rackingArrayLoc)
randomCheck2 = random.choice(rackingArrayLoc)
randomCheck3 = random.choice(rackingArrayLoc)
randomCheck4 = random.choice(rackingArrayLoc)
randomCheck5 = random.choice(rackingArrayLoc)
randomCheck6 = random.choice(rackingArrayLoc)
randomCheck7 = random.choice(rackingArrayLoc)
randomCheck8 = random.choice(rackingArrayLoc)
randomCheck9 = random.choice(rackingArrayLoc)
randomCheck10 = random.choice(rackingArrayLoc)

randomLetter1 = random.choice(rackingLetters)
randomLetter2 = random.choice(rackingLetters)
randomLetter3 = random.choice(rackingLetters)
randomLetter4 = random.choice(rackingLetters)
randomLetter5 = random.choice(rackingLetters)
randomLetter6 = random.choice(rackingLetters)
randomLetter7 = random.choice(rackingLetters)
randomLetter8 = random.choice(rackingLetters)
randomLetter9 = random.choice(rackingLetters)
randomLetter10 = random.choice(rackingLetters)
print(datetime.datetime.now())
print("This program will generate 10 random locations in order to eliminate bias and ensure a 'Truly Random' choice is selected")
print("The 10 Locations are:")


print(randomCheck1 + "-" + randomLetter1)
print(randomCheck2 + "-" + randomLetter2)
print(randomCheck3 + "-" + randomLetter3)
print(randomCheck4 + "-" + randomLetter4)
print(randomCheck5 + "-" + randomLetter5)
print(randomCheck6 + "-" + randomLetter6)
print(randomCheck7 + "-" + randomLetter7)
print(randomCheck8 + "-" + randomLetter8)
print(randomCheck9 + "-" + randomLetter9)
print(randomCheck10 + "-" + randomLetter10)

#isCorrect checks


print("Did the locations hold the correct stock? Please answer Y / N")

isCorrect1 = input(randomCheck1 + "-" + randomLetter1 + ":")
isCorrect2  = input(randomCheck2 + "-" + randomLetter2 + ":")
isCorrect3  = input(randomCheck3 + "-" + randomLetter3 + ":")
isCorrect4  = input(randomCheck4 + "-" + randomLetter4 + ":")
isCorrect5  = input(randomCheck5 + "-" + randomLetter5 + ":")
isCorrect6  = input(randomCheck6 + "-" + randomLetter6 + ":")
isCorrect7  = input(randomCheck7 + "-" + randomLetter7 + ":")
isCorrect8  = input(randomCheck8 + "-" + randomLetter8 + ":")
isCorrect9  = input(randomCheck9 + "-" + randomLetter9 + ":")
isCorrect10  = input(randomCheck10 + "-" + randomLetter10 + ":")

#Print log file for digital records


f = open(fileName, "x")
f.write(randomCheck1 + "-" + randomLetter1+ ": " + isCorrect1 + "\n")
f.write(randomCheck2 + "-" + randomLetter2 + ": " + isCorrect2 + "\n")
f.write(randomCheck3 + "-" + randomLetter3 + ": " + isCorrect3 + "\n")
f.write(randomCheck4 + "-" + randomLetter4 + ": " + isCorrect4 + "\n")
f.write(randomCheck5 + "-" + randomLetter5 + ": " + isCorrect5 + "\n")
f.write(randomCheck6 + "-" + randomLetter6 + ": " + isCorrect6 + "\n")
f.write(randomCheck7 + "-" + randomLetter7 + ": " + isCorrect7 + "\n")
f.write(randomCheck8 + "-" + randomLetter8 + ": " + isCorrect8 + "\n")
f.write(randomCheck9 + "-" + randomLetter9 + ": " + isCorrect9 + "\n")
f.write(randomCheck10 + "-" + randomLetter10 + ": " + isCorrect10 + "\n")


print("The results have been saved to the directory.")
print("Press enter to exit.")
input()
