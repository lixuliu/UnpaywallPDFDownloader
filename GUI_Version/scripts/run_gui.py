#!/usr/bin/env python3
"""
Simple launcher for the UnpaywallPDFDownloader GUI
"""

import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from UnpaywallPDFDownloader_GUI import main
    print("Starting Unpaywall PDF Downloader GUI...")
    main()
except ImportError as e:
    print(f"Error importing GUI module: {e}")
    print("Please make sure all dependencies are installed:")
    print("pip install -r requirements.txt")
except Exception as e:
    print(f"Error starting GUI: {e}")
