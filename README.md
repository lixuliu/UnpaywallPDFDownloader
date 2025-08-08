# Unpaywall PDF Downloader

This repository contains two versions of the Unpaywall PDF Downloader tool:

## 📁 Project Structure

```
UnpaywallPDFDownloader/
├── GUI_Version/                    # GUI Version (Recommended)
│   ├── src/                        # Source code
│   ├── scripts/                    # Utility scripts
│   ├── docs/                       # Documentation
│   ├── examples/                   # Example files
│   ├── venv/                       # Virtual environment
│   ├── launch_gui.py               # GUI launcher
│   ├── requirements.txt            # Dependencies
│   └── README.md                   # GUI documentation
├── UnpaywallPDFDownloader.py       # Original CLI version
├── requirements.txt                # CLI dependencies
├── README.md                       # This file
├── LICENSE.md                      # License information
├── NOTICE.md                       # Usage notice
├── METADATA.txt                    # Project metadata
├── Commercial Use Guidelines.md    # Commercial usage
└── index.html                      # Web interface example
```

## 🎯 Available Versions

### 🖥️ GUI Version (Recommended)

- **Location**: `GUI_Version/`
- **Features**: Modern graphical user interface with buttons, progress bars, and easy configuration
- **Best for**: Most users who prefer visual interfaces
- **Quick Start**:
  ```bash
  cd GUI_Version
  ./scripts/activate_env.sh
  python launch_gui.py
  ```

### 🖥️ CLI Version (Original)

- **Location**: Root directory
- **Features**: Command-line interface for technical users
- **Best for**: Advanced users, automation, and server environments
- **Quick Start**:
  ```bash
  pip install -r requirements.txt
  # Edit UnpaywallPDFDownloader.py to configure settings
  python UnpaywallPDFDownloader.py
  ```

## 🚀 Quick Start

### For GUI Version (Recommended)

1. **Navigate to GUI folder:**

   ```bash
   cd GUI_Version
   ```

2. **Set up environment:**

   ```bash
   ./scripts/activate_env.sh
   ```

3. **Launch GUI:**
   ```bash
   python launch_gui.py
   ```

### For CLI Version

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure the script:**
   Edit `UnpaywallPDFDownloader.py` and modify these variables:

   ```python
   api_email = "your.email@example.com"  # Your email for Unpaywall API
   download_dir = "path/to/your/download/directory"  # Download location
   csv_file_path = "path/to/your/dois.csv"  # Your CSV file with DOIs
   ```

3. **Run the script:**
   ```bash
   python UnpaywallPDFDownloader.py
   ```

## 📋 Features

Both versions provide:

- **DOI-based PDF fetching** using the Unpaywall API
- **Progress tracking** and error handling
- **CSV logging** of failed downloads
- **Sound notifications** on completion

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
