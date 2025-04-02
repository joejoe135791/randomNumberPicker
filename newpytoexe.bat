@echo off
nuitka --onefile main.py --enable-plugin=tk-inter
python copyjsons.py
echo exe (should) be created, don't forget to duplicate the numbers and config jsons in case they werent automatically! press enter to close
pause
exit