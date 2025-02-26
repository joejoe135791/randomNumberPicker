import os
import json
import sys
import random
import obsws_python as obs
from tkinter import *
from tkinter import messagebox 
from termcolor import cprint

if os.path.isfile(f"{os.getcwd()}/config.json") != True:
    root = Tk()
    root.wm_attributes("-topmost", 1)
    root.withdraw()
    messagebox.showerror("ERROR", "config.json not found!",parent=root) 
    sys.exit("config.json not found!")
if os.path.isfile(f"{os.getcwd()}/data.json") != True:
    root = Tk()
    root.wm_attributes("-topmost", 1)
    root.withdraw()
    messagebox.showerror("ERROR", "data.json not found!",parent=root) 
    sys.exit("data.json not found!")
loadedConfigJson = json.load(open("config.json"))
debugKaraokeMode = loadedConfigJson['debugMode']
removeFromList = loadedConfigJson['removeFromList']
versionNumber = loadedConfigJson['version']
minRandomAmount = loadedConfigJson['minRandomAmount']
maxRandomAmount = loadedConfigJson['maxRandomAmount']
currentSelectedMode = loadedConfigJson['currentMode'].casefold() # Set in config.json. Types are default (picks 1) and vs (picks 2, meant for tournaments)
showWelcomeMessage = loadedConfigJson['showWelcomeMessage']
celebrateWhenEmpty = loadedConfigJson['celebrateWhenEmpty']
customCelebrationMessage = loadedConfigJson['customCelebrationMessage']
obsJsonConfig = loadedConfigJson['websocketOBSSettings']
if obsJsonConfig['useOBSWebsocket'] == True:
    useOBSWebsocket = True
    websocketHostOBS = obsJsonConfig['hostOBS']
    # OBS port check & assignment
    if type(obsJsonConfig['portOBS']) != int:
        root = Tk()
        root.wm_attributes("-topmost", 1)
        root.withdraw()
        messagebox.showerror("ERROR", "OBS websocket port is not an integer",parent=root) 
        sys.exit("OBS websocket port is not an integer")
    else:
        websocketPortOBS = obsJsonConfig['portOBS']
    # OBS timeout check & assignment
    if type(obsJsonConfig['timeoutOBS']) != int:
        root = Tk()
        root.wm_attributes("-topmost", 1)
        root.withdraw()
        messagebox.showerror("ERROR", "OBS timeout duration is not an integer",parent=root) 
        sys.exit("OBS timeout duration is not an integer")
    else:
        websocketTimeoutOBS = obsJsonConfig['timeoutOBS']
    # Password check
    if obsJsonConfig['useWebsocketPassword'] == True:
        useWebsocketPassword = True
        if obsJsonConfig['websocketPasswordOBS'] == "Change Me if you use a password for your websocket. Make sure to set 'useWebsocketPassword' to true":
            root = Tk()
            root.wm_attributes("-topmost", 1)
            root.withdraw()
            messagebox.showerror("ERROR", "OBS websocket password is enabled but password is default, change in config.json",parent=root) 
            sys.exit("OBS websocket password is enabled but password is default, change in config.json")
        else:
            websocketPasswordOBS = obsJsonConfig['websocketPasswordOBS']
        clientOBS = obs.ReqClient(host=websocketHostOBS, port=websocketPortOBS, password=websocketPasswordOBS, timeout=websocketTimeoutOBS)
    else:
        # Add connection stuff from library - https://pypi.org/project/obsws-python
        clientOBS = obs.ReqClient(host=websocketHostOBS, port=websocketPortOBS, timeout=websocketTimeoutOBS)

i = 0
os.system('color')
loadedNumberJson = json.load(open("data.json"))
loadedNumberListData = loadedNumberJson["data"]
randomWhileAmount = random.randint(minRandomAmount, maxRandomAmount)
# Checking if data is not empty
if not loadedNumberListData:
    if celebrateWhenEmpty == True:
        root = Tk()
        root.wm_attributes("-topmost", 1)
        root.withdraw()
        messagebox.showinfo("CONGRATS", customCelebrationMessage,parent=root) 
        sys.exit("List is empty, add data to data.json file!")
    else:
        root = Tk()
        root.wm_attributes("-topmost", 1)
        root.withdraw()
        messagebox.showerror("ERROR", "List is empty, add data to data.json file!",parent=root) 
        sys.exit("List is empty, add data to data.json file!")
# Backup old data just in case
with open("oldData.json", "w") as outfile:
    json.dump(loadedNumberJson, outfile, indent=4, sort_keys=True)
# Shows welcome message
if showWelcomeMessage == True:
    welcomeMessage = f"""Welcome to the random data picker {versionNumber} by joejoe

In case the script ever deletes all json data. all data has been backed up to oldData.json. DO NOT RUN THE SCRIPT AGAIN BEFORE VERIFYING THE ORIGINAL JSON FILE!
press OK to continue"""
    cprint(welcomeMessage, "light_yellow")
    root = Tk()
    root.wm_attributes("-topmost", 1)
    root.withdraw()
    messagebox.showwarning("Welcome!", welcomeMessage,parent=root)
    root.destroy()
if debugKaraokeMode == True:
    cprint("Debugging enabled!", "light_yellow", attrs=['bold'])
    cprint(f"Amount to randomize: {randomWhileAmount}", "blue")
    cprint(f"loaded JSON Data\n{loadedNumberListData}", "blue")
    cprint(f"Current Selected Mode: {currentSelectedMode}", "blue")
    input("Press any button to continue")
else:
    pass
if currentSelectedMode == "default":
    while (i < randomWhileAmount):
        i += 1
        selectedChoiceData = random.choice(loadedNumberListData)
        if debugKaraokeMode == True:
            cprint(f"While loop has run {i}/{randomWhileAmount} times and has selected {selectedChoiceData}", "blue")

    root = Tk()
    root.wm_attributes("-topmost", 1)
    root.withdraw()
    messagebox.showinfo(f"Selected {selectedChoiceData}", f"Selected: {selectedChoiceData}.\npress ok to close",parent=root) 
    root.destroy()
    print(f"Selected {selectedChoiceData}")
    if removeFromList == True:
        loadedNumberListData.remove(selectedChoiceData)
        newJsonData = dict(data = loadedNumberListData)
        if debugKaraokeMode == True:
            cprint(f"New Json Data:\n{newJsonData}", "blue")
        with open("data.json", "w") as outfile:
            json.dump(newJsonData, outfile, indent=4, sort_keys=True)
        print(f"{selectedChoiceData} has been removed from list")
    sys.exit("Program has finished running")
elif currentSelectedMode == "vs":
    while (i < randomWhileAmount):
        i += 1
        selectedChoiceData = random.choice(loadedNumberListData)
        selectedChoiceData2 = random.choice(loadedNumberListData)
        if (i == randomWhileAmount) and (selectedChoiceData == selectedChoiceData2):
            i -= 1
        if debugKaraokeMode == True:
            cprint(f"While loop has run {i}/{randomWhileAmount} times and has selected {selectedChoiceData} VS {selectedChoiceData2}", "blue")

    root = Tk()
    root.wm_attributes("-topmost", 1)
    root.withdraw()
    messagebox.showinfo(f"{selectedChoiceData} VS {selectedChoiceData2}", f"{selectedChoiceData} VS {selectedChoiceData2}.\nPress OK to close",parent=root) 
    print(f"{selectedChoiceData} VS {selectedChoiceData2}")
    root.destroy()
    if removeFromList == True:
        loadedNumberListData.remove(selectedChoiceData)
        loadedNumberListData.remove(selectedChoiceData2)
        newJsonData = dict(data = loadedNumberListData)
        if debugKaraokeMode == True:
            cprint(f"New Json Data:\n{newJsonData}", "blue")
        with open("data.json", "w") as outfile:
            json.dump(newJsonData, outfile, indent=4, sort_keys=True)
        print(f"{selectedChoiceData} and {selectedChoiceData2} have been removed from list")
    sys.exit("Program has finished running")
else:
    root = Tk()
    root.wm_attributes("-topmost", 1)
    root.withdraw()
    messagebox.showerror("ERROR", f"Current Selected Mode {currentSelectedMode} IS NOT RECOGNIZED!\nChange in config.json",parent=root)
    root.destroy()
    sys.exit(f"Current Selected Mode {currentSelectedMode} IS NOT RECOGNIZED!\nChange in config.json")