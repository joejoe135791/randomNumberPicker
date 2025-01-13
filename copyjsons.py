import os
import sys
import shutil
from termcolor import cprint

currentWorkingDirectory = os.getcwd()
compiledExeDest = f"{currentWorkingDirectory}/compiledexe"
dataJsonFile = f"{currentWorkingDirectory}/data.json"
configJsonFile = f"{currentWorkingDirectory}/config.json"
os.system('color')

cprint(f"Copying {dataJsonFile} to {compiledExeDest}", "light_green")
try:
    shutil.copy2(configJsonFile, compiledExeDest)
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