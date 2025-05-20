# UnpaywallPDFDownloader

A Python script that automates the process of downloading open-access research articles in PDF format using DOIs (Digital Object Identifiers) retrieved from a CSV file. The script utilizes the Unpaywall API to check the availability of open-access versions of the articles and downloads them to a specified directory.

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

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

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
