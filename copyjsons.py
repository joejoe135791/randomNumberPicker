import os
import sys
import shutil
from termcolor import cprint

questionsAsked = False
currentWorkingDirectory = os.getcwd()
compiledExeDestRoot = f"{currentWorkingDirectory}/compiledexe"
dataJsonFile = f"{currentWorkingDirectory}/data.json"
configJsonFile = f"{currentWorkingDirectory}/config.json"
os.system('color')

def compilerQuestions():
    global compiledExeDest
    global questionsAsked
    compilerAnswer = input("What compiler are you using? Press 1 for pyinstaller or 2 for nuitka: ")
    if compilerAnswer == 1:
        compiledExeDest = f"{compiledExeDest}/nuitka"
    elif compilerAnswer == 2:
        compiledExeDest = f"{compiledExeDest}/pyinstaller"
    else:
        sys.exit(f"'{compilerAnswer}' is unknown, script exiting! please rerun the script from movejsons.bat")

def copyJsonsToNewDir():
    cprint(f"Copying {dataJsonFile} to {compiledExeDest}", "light_green")
    try:
        shutil.copy2(dataJsonFile, compiledExeDest)
    except FileExistsError:
        cprint(f"File already exists, skipping!", "light_red")
    except Exception as e:
        sys.exit(f"An error occurred, {e}")
    else:
        cprint(f"Copied {dataJsonFile} to {compiledExeDest}!", "light_green")

    cprint(f"Copying {configJsonFile} to {compiledExeDest}", "light_green")
    try:
        shutil.copy2(configJsonFile, compiledExeDest)
    except FileExistsError:
        cprint(f"File already exists, skipping!", "light_red")
    except Exception as e:
        sys.exit(f"An error occurred, {e}")
    else:
        cprint(f"Copied {configJsonFile} to {compiledExeDest}!", "light_green")
    sys.exit("Files moved, script exiting")

if questionsAsked == False:
    compilerQuestions()
else:
    copyJsonsToNewDir()