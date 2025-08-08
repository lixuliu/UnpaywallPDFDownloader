#!/usr/bin/env python3
"""
Test script for the UnpaywallPDFDownloader GUI
This script tests that the GUI can be imported and initialized without errors.
"""

import sys
import os

def test_gui_import():
    """Test that the GUI module can be imported"""
    try:
        import sys
        import os
        # Add src directory to path
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))
        from UnpaywallPDFDownloader_GUI import UnpaywallPDFDownloaderGUI
        print("✅ GUI module imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Failed to import GUI module: {e}")
        return False

def test_gui_initialization():
    """Test that the GUI can be initialized (without showing window)"""
    try:
        import tkinter as tk
        import sys
        import os
        # Add src directory to path
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))
        from UnpaywallPDFDownloader_GUI import UnpaywallPDFDownloaderGUI
        
        # Create a root window but don't show it
        root = tk.Tk()
        root.withdraw()  # Hide the window
        
        # Initialize the GUI
        app = UnpaywallPDFDownloaderGUI(root)
        
        # Clean up
        root.destroy()
        
        print("✅ GUI initialized successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to initialize GUI: {e}")
        return False

def test_dependencies():
    """Test that all required dependencies are available"""
    dependencies = [
        'tkinter',
        'pandas',
        'requests',
        'tqdm',
        'librosa',
        'sounddevice',
        'numpy',
        'json',
        'threading',
        'logging'
    ]
    
    missing = []
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"✅ {dep} available")
        except ImportError:
            print(f"❌ {dep} missing")
            missing.append(dep)
    
    if missing:
        print(f"\n❌ Missing dependencies: {', '.join(missing)}")
        return False
    else:
        print("\n✅ All dependencies available")
        return True

def main():
    """Run all tests"""
    print("Testing UnpaywallPDFDownloader GUI...")
    print("=" * 50)
    
    # Test dependencies
    deps_ok = test_dependencies()
    print()
    
    # Test GUI import
    import_ok = test_gui_import()
    print()
    
    # Test GUI initialization
    init_ok = test_gui_initialization()
    print()
    
    # Summary
    print("=" * 50)
    if deps_ok and import_ok and init_ok:
        print("🎉 All tests passed! GUI is ready to use.")
        print("\nTo run the GUI:")
        print("  python UnpaywallPDFDownloader_GUI.py")
        return True
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
