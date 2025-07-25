@echo off
REM Warframe Void Relics Simulator - First Time Setup Script
REM This script installs Flask (if needed) and runs the app.

echo === Warframe Void Relics Simulator Setup ===
echo.
echo Please make sure:
echo - Python is installed (https://www.python.org/downloads/)
echo - Python and pip are added to your system PATH
echo - You may need to restart your computer after installing Python
echo - You may need to run this script as administrator to install packages
echo.
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not in PATH. Please install Python and add it to your PATH.
    pause
    exit /b
)

pip --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo pip is not installed or not in PATH. Please install pip and add it to your PATH.
    pause
    exit /b
)

pip show flask >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Installing Flask...
    pip install flask
)

echo Starting the app...
python app.py

echo.
echo If the app did not start:
echo - Make sure Python and pip are installed and in your PATH
echo - Check for error messages above
echo - You may need to run this script as administrator
echo - You may need to restart your computer after installing Python
pause
