import os
import webbrowser
import json
import sys
import random
from tkinter import *
from tkinter import messagebox 
from termcolor import cprint

def addDataToList(DataName):
    pass

def removeDataFromList(dataName):
    pass

def homePage():
    while True:
        cprint("Press 1 to add, remove, and/or edit data entries to the list")
        cprint("Press 2 to add, remove and/or edit links")
        cprint("Press 3 to edit the configuration file")
        cprint("Press 4 to save changes to file")
        cprint("Press 0 to exit")
        selectedPage = input("Enter selection: ")
        if selectedPage == 1:
            pass
            break
        elif selectedPage == 2:
            pass
            break
        elif selectedPage == 3:
            pass
            break
        elif selectedPage == 4:
            saveData()
            break
        elif selectedPage == 0:
            sys.exit("You have exited the program")
            break

def editDataPage():
    pass

def editLinksPage():
    pass

def editConfigPage():
    pass

def loadData():
    pass

def saveData():
    pass

def theClaw(): # This is similar to a watchdog process, it just causes the program to loop and a couple other housekeeping tasks
    cprint('Initializing, please wait...')
    loadData()
    homePage()