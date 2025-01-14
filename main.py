import os
import json
import sys
import random
from tkinter import *
from tkinter import messagebox 
from termcolor import cprint

loadedConfigJson = json.load(open("config.json"))
debugKaraokeMode = loadedConfigJson['debugMode']
versionNumber = loadedConfigJson['version']
i = 0
os.system('color')
loadedNumberJson = json.load(open("data.json"))
loadedNumberListData = loadedNumberJson["data"]
randomWhileAmount = random.randint(1, 25)
# Backup old data just in case
with open("oldData.json", "w") as outfile:
    json.dump(loadedNumberJson, outfile, indent=4, sort_keys=True)

print(f"Welcome to the random data picker {versionNumber} by joejoe, designed for karaoke challenges, numbers, names and whatever you want to use it for")
cprint("In case the script ever deletes json data. all data has been backed up to oldData.json. DO NOT RUN THE SCRIPT AGAIN BEFORE VERIFYING THE ORIGINAL JSON FILE!", "light_yellow", attrs=['bold'])
if debugKaraokeMode == True:
    cprint("Debugging enabled!", "light_yellow", attrs=['bold'])
    cprint(f"Amount to randomize: {randomWhileAmount}", "blue")
    cprint(f"loaded JSON Data\n{loadedNumberListData}", "blue")
    input("Press any button to continue")
else:
    pass

while (i < randomWhileAmount):
    i += 1
    selectedNumber = random.choice(loadedNumberListData)
    if debugKaraokeMode == True:
        cprint(f"While loop has run {i}/{randomWhileAmount} times and has selected {selectedNumber}", "blue")

root = Tk()
root.withdraw()
root.geometry("300x200")
messagebox.showinfo(f"Selected {selectedNumber}", f"Selected: {selectedNumber}.\npress ok to remove {selectedNumber} from list") 
print(f"Selected number {selectedNumber}")

removedNumberList = loadedNumberListData.remove(selectedNumber)
newJsonData = dict(data = removedNumberList)
with open("data.json", "w") as outfile:
    json.dump(loadedNumberJson, outfile, indent=4, sort_keys=True)
print(f"{selectedNumber} has been removed from list")