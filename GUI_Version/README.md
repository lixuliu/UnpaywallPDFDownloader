# Unpaywall PDF Downloader

A Python tool that automates the process of downloading open-access research articles in PDF format using DOIs (Digital Object Identifiers) retrieved from a CSV file. The tool utilizes the Unpaywall API to check the availability of open-access versions of the articles and downloads them to a specified directory.

## 🎯 Features

- **DOI-based PDF fetching**: Automatically fetches and downloads PDFs using the Unpaywall API
- **Progress tracking**: Visualizes the download progress with a progress bar using tqdm
- **Error handling**: Logs and handles errors such as missing DOIs, failed downloads, and unavailable open-access versions
- **Sound notification**: Plays a notification sound upon completion of all downloads
- **CSV logging**: Failed downloads are recorded in a separate CSV file for easy follow-up
- **Modern GUI**: User-friendly graphical interface with real-time progress tracking

## 📁 Project Structure

```
UnpaywallPDFDownloader/
├── src/                           # Source code
│   └── UnpaywallPDFDownloader_GUI.py  # GUI application
├── scripts/                       # Utility scripts
│   ├── activate_env.sh           # macOS/Linux environment activation
│   ├── activate_env.bat          # Windows environment activation
│   ├── run_gui.py                # GUI launcher
│   └── test_gui.py               # Test script
├── docs/                         # Documentation
│   ├── GUI_README.md             # GUI documentation
│   ├── SETUP_COMPLETE.md         # Setup guide
│   ├── LICENSE.md                # License information
│   ├── NOTICE.md                 # Usage notice
│   ├── METADATA.txt              # Project metadata
│   └── Commercial Use Guidelines.md  # Commercial use guidelines
├── examples/                     # Example files
│   └── index.html                # Web interface example
├── venv/                         # Virtual environment (created automatically)
├── launch_gui.py                 # Main GUI launcher
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🚀 Quick Start

1. **Set up the environment:**

   ```bash
   # On macOS/Linux:
   ./scripts/activate_env.sh

   # On Windows:
   scripts\activate_env.bat
   ```

2. **Launch the GUI:**
   ```bash
   python launch_gui.py
   ```

## 📋 Requirements

- Python 3.6 or higher
- Required Python packages (automatically installed):
  - pandas
  - requests
  - tqdm
  - librosa
  - sounddevice
  - numpy

## 📖 Usage

### CSV File Format

Your CSV file should contain a column named 'DOI' with the Digital Object Identifiers. You can export this data from:

- **Scopus**: Export search results as CSV, ensuring DOI is included
- **Web of Science**: Export search results as CSV, ensuring DOI is included

Example CSV format:

```csv
DOI,Title,Authors
10.1038/nature12345,Example Paper,John Doe
10.1000/example.2023.001,Jane Smith
```

### GUI Features

The GUI provides:

- **Email Configuration**: Enter your email for the Unpaywall API
- **File Selection**: Browse and select CSV files with DOIs
- **Download Directory**: Choose where to save PDF files
- **Progress Tracking**: Real-time progress bar and status updates
- **Statistics**: Live count of total, downloaded, and failed articles
- **Log Display**: Real-time logging with timestamps
- **Configuration Persistence**: Saves your settings automatically

## 🔧 Development

### Testing

Run the test script to verify everything works:

```bash
python scripts/test_gui.py
```

### Environment Management

The project uses a virtual environment to isolate dependencies:

- **Activate**: `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows)
- **Deactivate**: `deactivate`
- **Reinstall dependencies**: `pip install -r requirements.txt`

## 📄 License

Creative Commons Attribution 4.0 International (CC BY 4.0)

## 📚 Citation

If you use this tool in your research, please cite it as follows:

```
@software{UnpaywallPDFDownloader,
  author = {Liu, Lixu},
  title = {UnpaywallPDFDownloader},
  year = {2024},
  url = {https://github.com/lixuliu/UnpaywallPDFDownloader}
}
```

Related DOI: https://doi.org/10.25500/edata.bham.00001292

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Contact

For questions or support, please contact: lixu@verdemetrix.com

## 📖 Additional Documentation

- [GUI Documentation](docs/GUI_README.md) - Detailed GUI usage guide
- [Setup Guide](docs/SETUP_COMPLETE.md) - Complete setup instructions
- [Commercial Use Guidelines](docs/Commercial%20Use%20Guidelines.md) - Commercial usage information
