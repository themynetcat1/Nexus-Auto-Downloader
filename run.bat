@echo off
title Nexus Mods & Vortex Auto-Downloader
setlocal

:: Step 1: Detect 'py' or 'python' command
py --version >nul 2>&1
if %errorlevel% equ 0 (
    set "PY_CMD=py"
    goto :found
)

python --version >nul 2>&1
if %errorlevel% equ 0 (
    set "PY_CMD=python"
    goto :found
)

:: If Python is not found on the system
cls
echo [ERROR] Python was not found on your system!
echo.
echo Solutions:
echo 1. If you do not want to install Python, simply use 'Launch.bat' (Portable version).
echo 2. If you want to use Python, ensure "Add Python to PATH" is checked during installation from python.org.
echo.
pause
exit /b

:found
echo Python found: %PY_CMD%
echo Checking and installing required dependencies...
%PY_CMD% -m pip install -r requirements.txt
cls
echo Starting script...
%PY_CMD% main.py
pause