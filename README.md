# UnpaywallPDFDownloader
This Python script automates the process of downloading open-access research articles in PDF format using DOIs (Digital Object Identifiers) retrieved from a CSV file. The script utilizes the Unpaywall API to check the availability of open-access versions of the articles and downloads them to a specified directory.

Features include:

	•	DOI-based PDF fetching: Automatically fetches and downloads PDFs using the Unpaywall API.
	•	Progress tracking: Visualizes the download progress with a progress bar using tqdm.
	•	Error handling: Logs and handles errors such as missing DOIs, failed downloads, and unavailable open-access versions.
	•	Sound notification: Plays a notification sound upon completion of all downloads.
	•	CSV logging: Failed downloads are recorded in a separate CSV file for easy follow-up.

Ideal for researchers looking to automate the collection of open-access articles for large datasets of DOIs.
