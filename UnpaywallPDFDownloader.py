import pandas as pd
import requests
import os
import logging
from requests.exceptions import RequestException
from tqdm import tqdm  # Progress bar for visualization
import librosa
import sounddevice as sd  # To play sound at the end of the process
import numpy as np

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Your email address for the Unpaywall API
api_email = "dsftliu@gmail.com"

# Directory where you want to save the downloaded PDFs
download_dir = "/Users/lixuliu/Desktop/Paper 2_Digital_Risk/Scopus/digital AND risk AND assessment/01"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Path to your CSV file
csv_file_path = "/Users/lixuliu/Desktop/Paper 2_Digital_Risk/Scopus/digital AND risk AND assessment/01.csv"

# Load the CSV file containing the DOIs
df = pd.read_csv(csv_file_path)

# Print the total number of articles to be downloaded
total_articles = len(df)
print(f"Total articles to be downloaded: {total_articles}")

# Initialize a list to store rows for articles that fail to download
failed_downloads = []

# Check if 'DOI' column exists in the CSV
if 'DOI' not in df.columns:
    logging.error("'DOI' column not found in CSV.")
else:
    # Iterate through the DOIs in the CSV with a progress bar
    for index, row in tqdm(df.iterrows(), total=total_articles, desc="Downloading articles"):
        doi = row['DOI']

        # Check if DOI is a valid string (not NaN)
        if pd.isna(doi) or not isinstance(doi, str):
            logging.warning(f"Invalid or missing DOI at row {index}, skipping.")
            failed_downloads.append(row)  # Save the row for failed downloads
            continue

        pdf_filename = os.path.join(download_dir, f"{doi.replace('/', '_')}.pdf")

        # Skip if PDF already exists
        if os.path.exists(pdf_filename):
            logging.info(f"PDF already exists for {doi}, skipping download.")
            continue

        api_url = f"https://api.unpaywall.org/v2/{doi}?email={api_email}"

        try:
            # Make an API request to Unpaywall with a User-Agent header
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            response = requests.get(api_url, headers=headers, timeout=10)

            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()

                # Check if an open-access version is available
                if data['is_oa'] and 'best_oa_location' in data:
                    pdf_url = data['best_oa_location']['url_for_pdf']

                    if pdf_url:
                        # Download the PDF
                        pdf_response = requests.get(pdf_url, headers=headers, timeout=10)

                        if pdf_response.status_code == 200 and 'application/pdf' in pdf_response.headers.get('Content-Type', ''):
                            # Save the PDF to the download directory
                            with open(pdf_filename, 'wb') as f:
                                f.write(pdf_response.content)
                            logging.info(f"Downloaded: {pdf_filename}")
                        else:
                            logging.warning(f"Failed to download PDF for {doi}, status code: {pdf_response.status_code}")
                            failed_downloads.append(row)  # Save the row for failed downloads
                    else:
                        logging.info(f"No open access PDF found for DOI {doi}")
                        failed_downloads.append(row)  # Save the row for failed downloads
                else:
                    logging.info(f"No open access version available for DOI {doi}")
                    failed_downloads.append(row)  # Save the row for failed downloads
            else:
                logging.error(f"Failed to retrieve data for DOI {doi}: HTTP {response.status_code}")
                failed_downloads.append(row)  # Save the row for failed downloads

        except RequestException as e:
            logging.error(f"Error processing DOI {doi}: {e}")
            failed_downloads.append(row)  # Save the row for failed downloads

# After processing all DOIs, save the failed downloads to a new CSV file
if failed_downloads:
    failed_df = pd.DataFrame(failed_downloads)
    failed_csv_path = os.path.join(os.path.dirname(csv_file_path), 'rest_articles.csv')
    failed_df.to_csv(failed_csv_path, index=False)
    logging.info(f"Saved failed downloads to {failed_csv_path}")
else:
    logging.info("All articles downloaded successfully.")

# Load a notification sound using librosa
notification_sound_path = librosa.example('trumpet')
sound_data, sampling_rate = librosa.load(notification_sound_path)

# Play the notification sound
sd.play(sound_data, sampling_rate)
sd.wait()  # Wait for the sound to finish playing

# Notify the user that the process is complete
print("Downloading process is complete! All articles downloaded.")