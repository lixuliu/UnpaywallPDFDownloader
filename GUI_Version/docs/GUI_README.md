# Unpaywall PDF Downloader - GUI Version

A modern graphical user interface for the UnpaywallPDFDownloader tool that automates the process of downloading open-access research articles in PDF format using DOIs from a CSV file.

## Features

### 🖥️ Modern GUI Interface

- Clean, intuitive user interface built with tkinter
- Real-time progress tracking with progress bar
- Live statistics (Total, Downloaded, Failed)
- Comprehensive logging display
- Configuration persistence

### 📁 Easy File Management

- Browse and select CSV files with DOI data
- Choose custom download directories
- Remember last used directories
- Open download folder directly from GUI

### ⚡ Enhanced Functionality

- Start/Stop download control
- Real-time status updates
- Error handling with user-friendly messages
- Sound notifications on completion
- Automatic saving of failed downloads

### 🔧 Configuration Management

- Save and load user preferences
- Email address for Unpaywall API
- Default download directory
- Last used file locations

## Installation

### Option 1: Isolated Environment (Recommended)

1. **Clone the repository:**

   ```bash
   git clone https://github.com/lixuliu/UnpaywallPDFDownloader.git
   cd UnpaywallPDFDownloader
   ```

2. **Set up isolated environment:**

   **On macOS/Linux:**

   ```bash
   ./activate_env.sh
   ```

   **On Windows:**

   ```cmd
   activate_env.bat
   ```

   This will:

   - Create a virtual environment in the project folder
   - Install all dependencies in the isolated environment
   - Keep your system Python environment clean

### Option 2: System-wide Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/lixuliu/UnpaywallPDFDownloader.git
   cd UnpaywallPDFDownloader
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Quick Start

1. **Activate the environment (if using isolated environment):**

   **On macOS/Linux:**

   ```bash
   source venv/bin/activate
   ```

   **On Windows:**

   ```cmd
   venv\Scripts\activate
   ```

2. **Run the GUI:**

   ```bash
   python UnpaywallPDFDownloader_GUI.py
   ```

   or

   ```bash
   python run_gui.py
   ```

3. **Configure the application:**

   - Enter your email address for the Unpaywall API
   - Select a CSV file containing DOIs
   - Choose a download directory

4. **Start downloading:**
   - Click "Start Download" to begin the process
   - Monitor progress in real-time
   - View detailed logs in the log section

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

## GUI Features

### Main Interface

- **Email Configuration**: Enter your email for the Unpaywall API
- **File Selection**: Browse and select your CSV file with DOIs
- **Download Directory**: Choose where to save the PDF files
- **Progress Tracking**: Real-time progress bar and status updates
- **Statistics**: Live count of total, downloaded, and failed articles

### Control Buttons

- **Start Download**: Begin the download process
- **Stop**: Interrupt the current download
- **Clear Log**: Clear the log display
- **Open Download Folder**: Open the download directory in file explorer

### Log Display

- Real-time logging of all operations
- Timestamped entries
- Error and warning messages
- Download status updates

## Configuration

The GUI automatically saves your configuration to `gui_config.json`:

- Email address for API
- Download directory
- Last used file locations

## Error Handling

The GUI provides comprehensive error handling:

- Input validation with helpful error messages
- Network error handling
- File access error handling
- Graceful handling of API failures

## Troubleshooting

### Common Issues

1. **"Email required" error:**

   - Make sure to enter a valid email address for the Unpaywall API

2. **"CSV file not found" error:**

   - Verify the CSV file path is correct
   - Ensure the file contains a 'DOI' column

3. **"Download directory not accessible" error:**

   - Check folder permissions
   - Ensure the directory exists or can be created

4. **Import errors:**
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Verify Python version (3.6 or higher)
   - If using isolated environment, ensure it's activated: `source venv/bin/activate` (macOS/Linux) or `venv\Scripts\activate` (Windows)

### Getting Help

If you encounter issues:

1. Check the log display for detailed error messages
2. Verify your CSV file format
3. Ensure your internet connection is stable
4. Check that your email address is valid

## System Requirements

- **Python**: 3.6 or higher
- **Operating System**: Windows, macOS, or Linux
- **Dependencies**: See requirements.txt

## License

Creative Commons Attribution 4.0 International (CC BY 4.0)

## Citation

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

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For questions or support, please contact: lixu@verdemetrix.com
