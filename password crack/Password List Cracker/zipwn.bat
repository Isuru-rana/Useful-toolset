@echo off
title Zipwn
color 3

if not exist "C:\Program Files\7-Zip" (
    echo 7-Zip not installed!
    pause
    exit
)

echo.
set /p archive="Enter Archive: "
if not exist "%archive%" (
    echo Archive not found!
    pause
    exit
)

set /p wordlist="Enter Wordlist: "
if not exist "%wordlist%" (
    echo Wordlist not found!
    pause
    exit
)

echo Cracking...
for /f "usebackq delims=" %%a in ("%wordlist%") do (
    set "pass=%%a"
    call :attempt
)
echo No valid password found. Check your wordlist.
pause
exit

:attempt
setlocal enabledelayedexpansion
set "safePass=!pass!"
"C:\Program Files\7-Zip\7z.exe" t -p"!safePass!" "%archive%" >nul 2>&1
echo ATTEMPT: "!safePass!"
if /I !errorlevel! EQU 0 (
    echo Success! Password Found: "!safePass!"
    pause
    exit
)
endlocal
