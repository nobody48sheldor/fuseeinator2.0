@echo off
color 2
cls

:menu
cls
ECHO * ----------                      FUSEEINATOR 2.0                   ---------- *
ECHO * --                                                                        -- *
ECHO * --                          hello %COMPUTERNAME%                          -- *
ECHO * -- chose your rocket  (type 1 or 2)                                       -- *
ECHO * --                                                                        -- *
ECHO * -- 1.Propergol Rocket                                                     -- *
ECHO * -- 2.Water Rocket                                                         -- *
ECHO * ---------------------------------------------------------------------------- *

SET /p m=-

ECHO %m% > type.txt
if %m% == 1 (GOTO :propergol)
if %m% == 2 (GOTO :water)
if %m% !==! 1 (if %m% !==! 2 (GOTO :menu))

:propergol
ECHO go to settings ? (yes/no)
SET /p sfi=-

if %sfi% == yes (GOTO :settingspropergol)
if %sfi% == no (
    cls
    python fuseeinator_runner.py
    GOTO :menu)
if %sfi% !==! yes (if %m% !==! no (GOTO :menu))

:settingspropergol
cls
ECHO * ------------------------------- FUSEEINATOR 2.0 ---------------------------- *
ECHO * --                                                                        -- *
ECHO * --                             set up your rocket                         -- *
ECHO * --                                                                        -- *
ECHO * --                                mass =                                  -- *
ECHO * --                      mass propergol =                                  -- *
ECHO * --                    propulsion force =                                  -- *
ECHO * --                     propulsion time =                                  -- *
ECHO * --                                  Cz =                                  -- *
ECHO * ---------------------------------------------------------------------------- *
ECHO enter parameters (separator is "/")
SET /p pfi=-
ECHO %pfi% > fi.txt
cls
python fuseeinator_runner.py
cls
GOTO :menu

:water

ECHO go to settings ? (yes/no)
SET /p swr=-

if %swr% == yes (GOTO :settingswaterrocket)
if %swr% == no (
    cls
    python waterrocket_runner.py
    GOTO :menu)
if %swr% !==! yes (if %m% !==! no (GOTO :menu))

:settingswaterrocket
cls
ECHO * ------------------------------- FUSEEINATOR 2.0 ---------------------------- *
ECHO * --                                                                        -- *
ECHO * --                             set up your rocket                         -- *
ECHO * --                                                                        -- *
ECHO * --                                mass =                                  -- *
ECHO * --                      mass propelent =                                  -- *
ECHO * --                            pressure =                                  -- *
ECHO * --                        rhoP(kg/m^3) =                                  -- *
ECHO * --                                  Cz =                                  -- *
ECHO * ---------------------------------------------------------------------------- *
ECHO enter parameters (separator is "/")
SET /p pwr=-
ECHO %pwr% > wr.txt
cls
python waterrocket_runner.py
cls
GOTO :menu
