#!/usr/bin/env python3
"""
UnpaywallPDFDownloader GUI

A graphical user interface for the UnpaywallPDFDownloader tool that automates
the process of downloading open-access research articles in PDF format using DOIs.

Author: Lixu Liu
Date: 2025-01-27
License: Creative Commons Attribution 4.0 International (CC BY 4.0)
Repository: https://github.com/lixuliu/UnpaywallPDFDownloader
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import pandas as pd
import requests
import os
import logging
import threading
from requests.exceptions import RequestException
from tqdm import tqdm
import librosa
import sounddevice as sd
import numpy as np
from datetime import datetime
import json

class UnpaywallPDFDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Unpaywall PDF Downloader")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # Set theme and styling
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configuration variables
        self.config_file = "gui_config.json"
        self.load_config()
        
        # Download state
        self.is_downloading = False
        self.download_thread = None
        
        self.setup_ui()
        self.load_config()
        
    def load_config(self):
        """Load configuration from JSON file"""
        default_config = {
            "api_email": "your.email@example.com",
            "download_dir": os.path.expanduser("~/Downloads/UnpaywallPDFs"),
            "csv_file_path": "",
            "last_used_dir": os.path.expanduser("~")
        }
        
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
            else:
                self.config = default_config
        except:
            self.config = default_config
            
    def save_config(self):
        """Save configuration to JSON file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            print(f"Error saving config: {e}")
    
    def setup_ui(self):
        """Setup the user interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Unpaywall PDF Downloader", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Email configuration
        ttk.Label(main_frame, text="Email for Unpaywall API:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.email_var = tk.StringVar(value=self.config.get("api_email", ""))
        email_entry = ttk.Entry(main_frame, textvariable=self.email_var, width=50)
        email_entry.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # CSV file selection
        ttk.Label(main_frame, text="CSV File with DOIs:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.csv_var = tk.StringVar(value=self.config.get("csv_file_path", ""))
        csv_entry = ttk.Entry(main_frame, textvariable=self.csv_var, width=40)
        csv_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        ttk.Button(main_frame, text="Browse", command=self.browse_csv).grid(row=2, column=2, padx=(10, 0))
        
        # Download directory selection
        ttk.Label(main_frame, text="Download Directory:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.download_dir_var = tk.StringVar(value=self.config.get("download_dir", ""))
        download_entry = ttk.Entry(main_frame, textvariable=self.download_dir_var, width=40)
        download_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        ttk.Button(main_frame, text="Browse", command=self.browse_download_dir).grid(row=3, column=2, padx=(10, 0))
        
        # Progress section
        progress_frame = ttk.LabelFrame(main_frame, text="Progress", padding="10")
        progress_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=20)
        progress_frame.columnconfigure(0, weight=1)
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, 
                                           maximum=100, length=400)
        self.progress_bar.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Status label
        self.status_var = tk.StringVar(value="Ready to download")
        status_label = ttk.Label(progress_frame, textvariable=self.status_var)
        status_label.grid(row=1, column=0, sticky=tk.W)
        
        # Statistics
        stats_frame = ttk.Frame(progress_frame)
        stats_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        
        self.total_var = tk.StringVar(value="Total: 0")
        self.downloaded_var = tk.StringVar(value="Downloaded: 0")
        self.failed_var = tk.StringVar(value="Failed: 0")
        
        ttk.Label(stats_frame, textvariable=self.total_var).grid(row=0, column=0, padx=(0, 20))
        ttk.Label(stats_frame, textvariable=self.downloaded_var).grid(row=0, column=1, padx=(0, 20))
        ttk.Label(stats_frame, textvariable=self.failed_var).grid(row=0, column=2)
        
        # Control buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=5, column=0, columnspan=3, pady=20)
        
        self.start_button = ttk.Button(button_frame, text="Start Download", 
                                      command=self.start_download, style='Accent.TButton')
        self.start_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.stop_button = ttk.Button(button_frame, text="Stop", 
                                     command=self.stop_download, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Button(button_frame, text="Clear Log", command=self.clear_log).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(button_frame, text="Open Download Folder", 
                  command=self.open_download_folder).pack(side=tk.LEFT)
        
        # Log section
        log_frame = ttk.LabelFrame(main_frame, text="Log", padding="10")
        log_frame.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(6, weight=1)
        
        # Log text area
        self.log_text = scrolledtext.ScrolledText(log_frame, height=15, width=80)
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure logging to GUI
        self.setup_logging()
        
    def setup_logging(self):
        """Setup logging to display in GUI"""
        class TextHandler(logging.Handler):
            def __init__(self, text_widget):
                logging.Handler.__init__(self)
                self.text_widget = text_widget
                
            def emit(self, record):
                msg = self.format(record)
                def append():
                    self.text_widget.insert(tk.END, msg + '\n')
                    self.text_widget.see(tk.END)
                self.text_widget.after(0, append)
        
        # Configure logging
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        
        # Clear existing handlers
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
        
        # Add GUI handler
        text_handler = TextHandler(self.log_text)
        text_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(text_handler)
        
    def browse_csv(self):
        """Browse for CSV file"""
        filename = filedialog.askopenfilename(
            title="Select CSV file with DOIs",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            initialdir=self.config.get("last_used_dir", os.path.expanduser("~"))
        )
        if filename:
            self.csv_var.set(filename)
            self.config["csv_file_path"] = filename
            self.config["last_used_dir"] = os.path.dirname(filename)
            self.save_config()
            
    def browse_download_dir(self):
        """Browse for download directory"""
        directory = filedialog.askdirectory(
            title="Select download directory",
            initialdir=self.config.get("download_dir", os.path.expanduser("~"))
        )
        if directory:
            self.download_dir_var.set(directory)
            self.config["download_dir"] = directory
            self.save_config()
            
    def validate_inputs(self):
        """Validate user inputs"""
        if not self.email_var.get().strip():
            messagebox.showerror("Error", "Please enter your email address for the Unpaywall API.")
            return False
            
        if not self.csv_var.get().strip():
            messagebox.showerror("Error", "Please select a CSV file containing DOIs.")
            return False
            
        if not os.path.exists(self.csv_var.get()):
            messagebox.showerror("Error", "The selected CSV file does not exist.")
            return False
            
        if not self.download_dir_var.get().strip():
            messagebox.showerror("Error", "Please select a download directory.")
            return False
            
        return True
        
    def start_download(self):
        """Start the download process in a separate thread"""
        if not self.validate_inputs():
            return
            
        if self.is_downloading:
            return
            
        self.is_downloading = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        
        # Save current configuration
        self.config["api_email"] = self.email_var.get()
        self.config["csv_file_path"] = self.csv_var.get()
        self.config["download_dir"] = self.download_dir_var.get()
        self.save_config()
        
        # Start download thread
        self.download_thread = threading.Thread(target=self.download_process)
        self.download_thread.daemon = True
        self.download_thread.start()
        
    def stop_download(self):
        """Stop the download process"""
        self.is_downloading = False
        self.status_var.set("Stopping download...")
        
    def download_process(self):
        """Main download process"""
        try:
            # Get configuration
            api_email = self.email_var.get()
            download_dir = self.download_dir_var.get()
            csv_file_path = self.csv_var.get()
            
            # Create download directory if it doesn't exist
            if not os.path.exists(download_dir):
                os.makedirs(download_dir)
                
            # Load CSV file
            try:
                df = pd.read_csv(csv_file_path)
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Error", f"Failed to read CSV file: {e}"))
                return
                
            # Check for DOI column
            if 'DOI' not in df.columns:
                self.root.after(0, lambda: messagebox.showerror("Error", "'DOI' column not found in CSV file."))
                return
                
            total_articles = len(df)
            downloaded_count = 0
            failed_count = 0
            failed_downloads = []
            
            # Update UI
            self.root.after(0, lambda: self.total_var.set(f"Total: {total_articles}"))
            self.root.after(0, lambda: self.status_var.set("Starting download..."))
            
            # Process each DOI
            for index, row in df.iterrows():
                if not self.is_downloading:
                    self.root.after(0, lambda: self.status_var.set("Download stopped by user"))
                    break
                    
                doi = row['DOI']
                
                # Update progress
                progress = ((index + 1) / total_articles) * 100
                self.root.after(0, lambda p=progress: self.progress_var.set(p))
                self.root.after(0, lambda i=index, t=total_articles: 
                              self.status_var.set(f"Processing {i+1}/{t}: {doi}"))
                
                # Check if DOI is valid
                if pd.isna(doi) or not isinstance(doi, str):
                    logging.warning(f"Invalid or missing DOI at row {index}, skipping.")
                    failed_count += 1
                    failed_downloads.append(row)
                    continue
                    
                pdf_filename = os.path.join(download_dir, f"{doi.replace('/', '_')}.pdf")
                
                # Skip if PDF already exists
                if os.path.exists(pdf_filename):
                    logging.info(f"PDF already exists for {doi}, skipping download.")
                    downloaded_count += 1
                    continue
                    
                # Make API request
                api_url = f"https://api.unpaywall.org/v2/{doi}?email={api_email}"
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
                
                try:
                    response = requests.get(api_url, headers=headers, timeout=10)
                    
                    if response.status_code == 200:
                        data = response.json()
                        
                        if data['is_oa'] and 'best_oa_location' in data:
                            pdf_url = data['best_oa_location']['url_for_pdf']
                            
                            if pdf_url:
                                pdf_response = requests.get(pdf_url, headers=headers, timeout=10)
                                
                                if pdf_response.status_code == 200 and 'application/pdf' in pdf_response.headers.get('Content-Type', ''):
                                    with open(pdf_filename, 'wb') as f:
                                        f.write(pdf_response.content)
                                    logging.info(f"Downloaded: {pdf_filename}")
                                    downloaded_count += 1
                                else:
                                    logging.warning(f"Failed to download PDF for {doi}")
                                    failed_count += 1
                                    failed_downloads.append(row)
                            else:
                                logging.info(f"No open access PDF found for DOI {doi}")
                                failed_count += 1
                                failed_downloads.append(row)
                        else:
                            logging.info(f"No open access version available for DOI {doi}")
                            failed_count += 1
                            failed_downloads.append(row)
                    else:
                        logging.error(f"Failed to retrieve data for DOI {doi}: HTTP {response.status_code}")
                        failed_count += 1
                        failed_downloads.append(row)
                        
                except Exception as e:
                    logging.error(f"Error processing DOI {doi}: {e}")
                    failed_count += 1
                    failed_downloads.append(row)
                    
                # Update statistics
                self.root.after(0, lambda d=downloaded_count: self.downloaded_var.set(f"Downloaded: {d}"))
                self.root.after(0, lambda f=failed_count: self.failed_var.set(f"Failed: {f}"))
                
            # Save failed downloads
            if failed_downloads:
                failed_df = pd.DataFrame(failed_downloads)
                # Save in the download directory with a more informative name
                failed_csv_path = os.path.join(download_dir, 'unretrieved_articles.csv')
                failed_df.to_csv(failed_csv_path, index=False)
                logging.info(f"Saved failed downloads to {failed_csv_path}")
                
            # Play notification sound
            try:
                notification_sound_path = librosa.example('trumpet')
                sound_data, sampling_rate = librosa.load(notification_sound_path)
                sd.play(sound_data, sampling_rate)
                sd.wait()
            except:
                pass  # Ignore sound errors
                
            # Update final status
            if self.is_downloading:
                self.root.after(0, lambda: self.status_var.set("Download completed!"))
                self.root.after(0, lambda: messagebox.showinfo("Complete", 
                    f"Download process completed!\n\n"
                    f"Total: {total_articles}\n"
                    f"Downloaded: {downloaded_count}\n"
                    f"Failed: {failed_count}"))
                    
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"An error occurred: {e}"))
            logging.error(f"Download process error: {e}")
        finally:
            self.is_downloading = False
            self.root.after(0, lambda: self.start_button.config(state=tk.NORMAL))
            self.root.after(0, lambda: self.stop_button.config(state=tk.DISABLED))
            
    def clear_log(self):
        """Clear the log text area"""
        self.log_text.delete(1.0, tk.END)
        
    def open_download_folder(self):
        """Open the download folder in file explorer"""
        download_dir = self.download_dir_var.get()
        if download_dir and os.path.exists(download_dir):
            os.system(f'open "{download_dir}"')  # macOS
        else:
            messagebox.showwarning("Warning", "Download directory does not exist.")

def main():
    """Main function to run the GUI application"""
    root = tk.Tk()
    app = UnpaywallPDFDownloaderGUI(root)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()
