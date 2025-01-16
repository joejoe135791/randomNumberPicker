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
minRandomAmount = loadedConfigJson['minRandomAmount']
maxRandomAmount = loadedConfigJson['maxRandomAmount']
currentSelectedMode = loadedConfigJson['currentMode']
showWelcomeMessage = loadedConfigJson['showWelcomeMessage']
i = 0
os.system('color')
loadedNumberJson = json.load(open("data.json"))
loadedNumberListData = loadedNumberJson["data"]
randomWhileAmount = random.randint(minRandomAmount, maxRandomAmount)
# Backup old data just in case
with open("oldData.json", "w") as outfile:
    json.dump(loadedNumberJson, outfile, indent=4, sort_keys=True)

if showWelcomeMessage == True:
    welcomeMessage = f"""Welcome to the random data picker {versionNumber} by joejoe

In case the script ever deletes all json data. all data has been backed up to oldData.json. DO NOT RUN THE SCRIPT AGAIN BEFORE VERIFYING THE ORIGINAL JSON FILE!
press OK to continue"""
    cprint(welcomeMessage, "light_yellow")
    root = Tk()
    root.withdraw()
    messagebox.showwarning("Welcome!", welcomeMessage)
if debugKaraokeMode == True:
    cprint("Debugging enabled!", "light_yellow", attrs=['bold'])
    cprint(f"Amount to randomize: {randomWhileAmount}", "blue")
    cprint(f"loaded JSON Data\n{loadedNumberListData}", "blue")
    cprint(f"Current Selected Mode: {currentSelectedMode}", "blue")
    input("Press any button to continue")
else:
    pass

while (i < randomWhileAmount):
    i += 1
    selectedChoiceData = random.choice(loadedNumberListData)
    if debugKaraokeMode == True:
        cprint(f"While loop has run {i}/{randomWhileAmount} times and has selected {selectedChoiceData}", "blue")

root = Tk()
root.withdraw()
# root.geometry("300x200")
messagebox.showinfo(f"Selected {selectedChoiceData}", f"Selected: {selectedChoiceData}.\npress ok to remove {selectedChoiceData} from list") 
print(f"Selected {selectedChoiceData}")

removedNumberList = loadedNumberListData.remove(selectedChoiceData)
newJsonData = dict(data = removedNumberList)
with open("data.json", "w") as outfile:
    json.dump(loadedNumberJson, outfile, indent=4, sort_keys=True)
print(f"{selectedChoiceData} has been removed from list")