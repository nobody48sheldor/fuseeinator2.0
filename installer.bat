@echo off
color 2
cls

git clone https://github.com/nobody48sheldor/fuseeinator2.0

cd position_calculation

ECHO this installation might take about 2 to 10 minutes
ECHO .
ECHO .

pip install pyinstaller

python -m PyInstaller --onefile -w --noconsole -F --icon=icon_software_2.ico fuseeinator_software_2.0_soft.py

cd dist

move fuseeinator_software_2.0_soft.exe ../..

cd ../..

SET /p m= Would you like to launch the software ? (Y or N)

if %m% == Y start fuseeinator_software_2.0_soft.exe
if %m% == N exit
if %m% !==! Y (if %m% !==! N (ECHO please enter a right answer (Y or N)))
