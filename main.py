import os
import json
import sys
import random
from tkinter import *
from tkinter import messagebox 
from termcolor import cprint

debugKaraokeMode = True
i = 0
os.system('color')
loadedNumberJson = json.load(open("numbers.json"))
loadedNumberListData = loadedNumberJson["numbers"]
randomWhileAmount = random.randint(1, 25)
# Backup old data just in case
with open("oldNumbers.json", "w") as outfile:
    json.dump(loadedNumberJson, outfile, indent=4, sort_keys=True)

print("Welcome to the Random Number picker by joejoeVT, designed for karaoke challenges")
cprint("In case the script ever deletes json data. all data has been backed up to oldNumbers.json. DO NOT RUN THE SCRIPT AGAIN BEFORE VERIFYING THE ORIGINAL JSON FILE!", "light_yellow", attrs=['bold'])
if debugKaraokeMode == True:
    cprint("Debugging enabled!", "light_yellow", attrs=['bold'])
    cprint(f"Amount to randomize: {randomWhileAmount}", "blue")
    cprint(f"loaded JSON Data\n{loadedNumberListData}", "blue")

while (i < randomWhileAmount):
    i += 1
    selectedNumber = random.choice(loadedNumberListData)
    if debugKaraokeMode == True:
        cprint(f"While loop has run {i}/{randomWhileAmount} times and has selected {selectedNumber}", "blue")

root = Tk()
root.withdraw()
root.geometry("300x200")
  
messagebox.showinfo(f"Selected Number {selectedNumber}", f"Selected Number: {selectedNumber}") 
print(f"Selected number {selectedNumber}")

removedNumberList = loadedNumberListData.remove(selectedNumber)
newJsonData = dict(numbers = removedNumberList)
with open("numbers.json", "w") as outfile:
    json.dump(loadedNumberJson, outfile, indent=4, sort_keys=True)
print(f"{selectedNumber} has been removed from list")