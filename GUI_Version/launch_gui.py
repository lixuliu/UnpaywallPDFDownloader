#!/usr/bin/env python3
"""
Main launcher for UnpaywallPDFDownloader GUI
This script launches the GUI application from the organized project structure.
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

def main():
    """Launch the GUI application"""
    try:
        from UnpaywallPDFDownloader_GUI import main as gui_main
        print("🚀 Launching Unpaywall PDF Downloader GUI...")
        gui_main()
    except ImportError as e:
        print(f"❌ Error importing GUI module: {e}")
        print("Please make sure the virtual environment is activated:")
        print("  source venv/bin/activate  # macOS/Linux")
        print("  venv\\Scripts\\activate     # Windows")
        print("\nOr run the setup script:")
        print("  ./scripts/activate_env.sh  # macOS/Linux")
        print("  scripts\\activate_env.bat   # Windows")
    except Exception as e:
        print(f"❌ Error launching GUI: {e}")

if __name__ == "__main__":
    main()
