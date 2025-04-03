@echo off
pyinstaller --onefile main.py -n RandomDataPicker -c --distpath ./compiledexe/pyinstaller
python copyjsons.py
echo exe (should) be created, don't forget to duplicate the numbers and config jsons in case they werent automatically! press enter to close
pause
exit