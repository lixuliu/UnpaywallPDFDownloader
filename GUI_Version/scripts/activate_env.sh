#!/bin/bash
# Activation script for UnpaywallPDFDownloader virtual environment

echo "Activating UnpaywallPDFDownloader virtual environment..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies if not already installed
if [ ! -f "venv/lib/python*/site-packages/pandas" ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

echo "Virtual environment activated!"
echo "You can now run: python UnpaywallPDFDownloader_GUI.py"
echo "To deactivate, run: deactivate"
