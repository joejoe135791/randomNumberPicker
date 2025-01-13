@echo off
pyinstaller --onefile main.py -n RandomDataPicker -c --distpath ./compiledexe
echo exe (should) be created, don't forget to duplicate the numbers and config jsons! press enter to close
pause
exit