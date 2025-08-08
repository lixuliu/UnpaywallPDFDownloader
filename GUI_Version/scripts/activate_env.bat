@echo off
REM Activation script for UnpaywallPDFDownloader virtual environment (Windows)

echo Activating UnpaywallPDFDownloader virtual environment...

REM Check if virtual environment exists
if not exist "venv" (
    echo Virtual environment not found. Creating one...
    python -m venv venv
)

REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Upgrade pip
python -m pip install --upgrade pip

REM Install dependencies if not already installed
if not exist "venv\Lib\site-packages\pandas" (
    echo Installing dependencies...
    pip install -r requirements.txt
)

echo Virtual environment activated!
echo You can now run: python UnpaywallPDFDownloader_GUI.py
echo To deactivate, run: deactivate
pause
