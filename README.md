# UnpaywallPDFDownloader

A Python script that automates the process of downloading open-access research articles in PDF format using DOIs (Digital Object Identifiers) retrieved from a CSV file. The script utilizes the Unpaywall API to check the availability of open-access versions of the articles and downloads them to a specified directory.

## Web Application

**🌐 Try the online version:** [OpenAccess PDF Downloader](https://www.openaccesspdfdownloader.verdemetrix.com)

For a user-friendly web application that doesn't require Python installation, visit the online version of this tool. Simply upload your CSV file with DOIs and download the PDFs directly from your browser.

## Support This Project

This project is available both as a **web application** at [openaccesspdfdownloader.verdemetrix.com](https://www.openaccesspdfdownloader.verdemetrix.com) and as open-source code for local use. If you find this tool useful for your research or work, please consider supporting its continued development and maintenance:

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ff69b4?logo=github)](https://github.com/sponsors/lixuliu) [![Ko-fi](https://img.shields.io/badge/Ko--fi-Buy%20me%20a%20coffee-ff5f5f?logo=ko-fi)](https://ko-fi.com/lixuliu)

Your donations help support:

- 🌐 **Web application maintenance** - Server costs, updates, and reliability
- 💻 **Local app interface development** - New features and improvements for the desktop version
- 🔧 Ongoing development and bug fixes for both platforms
- 📚 Keep documentation up-to-date
- ⚡ Ensure compatibility with latest APIs

Even small contributions make a big difference in keeping this project alive and useful for the research community!

## Features

- DOI-based PDF fetching: Automatically fetches and downloads PDFs using the Unpaywall API
- Progress tracking: Visualizes the download progress with a progress bar using tqdm
- Error handling: Logs and handles errors such as missing DOIs, failed downloads, and unavailable open-access versions
- Sound notification: Plays a notification sound upon completion of all downloads
- CSV logging: Failed downloads are recorded in a separate CSV file for easy follow-up

## Requirements

- Python 3.6 or higher
- Required Python packages (install via `pip install -r requirements.txt`):
  - pandas
  - requests
  - tqdm
  - librosa
  - sounddevice
  - numpy

## Installation

1. Clone this repository:

```bash
git clone https://github.com/lixuliu/UnpaywallPDFDownloader.git
cd UnpaywallPDFDownloader
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Prepare a CSV file containing a column named 'DOI' with the Digital Object Identifiers of the articles you want to download.
   You can export this data from:

   - Scopus: Export search results as CSV, ensuring DOI is included
   - Web of Science: Export search results as CSV, ensuring DOI is included

2. Configure the script by modifying these variables in `UnpaywallPDFDownloader.py`:

   ```python
   # Your email address for the Unpaywall API
   api_email = "your.email@example.com"  # Replace with your email

   # Directory where you want to save the downloaded PDFs
   download_dir = "path/to/your/download/directory"  # Replace with your desired path

   # Path to your CSV file
   csv_file_path = "path/to/your/dois.csv"  # Replace with your CSV file path
   ```

3. Run the script:

```bash
python UnpaywallPDFDownloader.py
```

## Output

- Successfully downloaded PDFs will be saved in the specified download directory
- Failed downloads will be recorded in a new CSV file named 'rest_articles.csv' in the same directory as the input CSV
- A notification sound will play when the process is complete
- Progress and error messages will be displayed in the console

## Error Handling

The script handles various error cases:

- Missing or invalid DOIs
- Network connection issues
- Unavailable open-access versions
- Failed PDF downloads

All errors are logged with appropriate messages in the console.

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

## LICENSE

Creative Commons Attribution 4.0 International (CC BY 4.0)

You are free to:

- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material for any purpose, even commercially

Under the following terms:

- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made.

No additional restrictions — you may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

For details, see the full license at: https://creativecommons.org/licenses/by/4.0/

Copyright © 2025 Dr. Lixu Liu

## NOTICE

This software is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

The author, Dr. Lixu Liu, welcomes copying, modification, integration, and collaboration.

This software is made available for both academic and commercial use, with the following expectations:

- **Attribution is required** in all public uses or integrations.
- **Direct resale or redistribution of the code or outputs without modification or added value is discouraged.**
- Modified versions should clearly indicate they differ from the original.

To acknowledge or notify the author, please contact: lixu@verdemetrix.com

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

# Commercial Use Guidelines

This project is licensed under the [Creative Commons Attribution 4.0 License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).  
You are free to use, share, and adapt the material — including in commercial projects — provided you give proper credit.

## Attribution Requirements

If you use this project (including as part of a paid product or service), you must visibly credit:

> Dr. Lixu Liu, University of Birmingham  
> "UnpaywallPDFDownloader"  
> https://github.com/lixuliu/UnpaywallPDFDownloader

## Respectful Use

Although commercial use is permitted by license, **the author discourages direct resale or redistribution** of this project without meaningful modification or added value.

### ✅ You may:

- Use or adapt the software in your paid platform or service
- Share modified versions with proper credit
- Reference or include the work in academic, consulting, or public sector projects

### ❌ Please do not:

- Sell or package the code "as-is"
- Repost the ZIP as a paid download
- Remove author attribution from outputs

For major commercial use or partnership discussions, please contact: info@verdemetrix.com
