@echo off
color 2
cls

ECHO this installation might take about 2 to 10 minutes
ECHO .
ECHO .

git clone https://github.com/nobody48sheldor/fuseeinator2.0

cd position_calculation

ECHO first installing the packge "pyinstaller" in order to compile the python code

pip install pyinstaller

ECHO .
ECHO .
ECHO compiling...

python -m PyInstaller --onefile -w --noconsole -F --icon=icon_software_2.ico fuseeinator_software_2.0_soft.py

cd dist

move fuseeinator_software_2.0_soft.exe ../..

cd ../..

SET /p z= Would you like to delete the unnecessary file (not developper "mode") ? (Y  or N)

if %z% == Y GOTO delete
if %z% == N GOTO software
if %z% !==! Y (if %m% !==! N (ECHO please enter a right answer (Y or N)))

:software
SET /p m= Would you like to launch the software ? (Y or N)

if %m% == Y start fuseeinator_software_2.0_soft.exe
if %m% == N exit
if %m% !==! Y (if %m% !==! N (ECHO please enter a right answer (Y or N)))

exit

:delete
cd position_calculation

del ROCKET_calculation.bat /q
del backup.txt /q
del fi.txt /q
del fucntion.py /q
del fuseeinator.py /q
del fuseeinator_runner.py /q
del fuseeinator_software.py /q
del fuseeinator_software.exe /q
del fuseeinator_software.spec /q
del fuseeinator_software_2.0.py /q
del fuseeinator_software_2.0_soft.py /q
del fuseeinator_software_2.0_soft.spec /q
del icon_software.ico /q
del icon_software.png /q
del icon_software_2.ico /q
del 'type.txt' /q
del waterrocket.py /q
del waterrocket_runner.py /q
del wr.txt/q
