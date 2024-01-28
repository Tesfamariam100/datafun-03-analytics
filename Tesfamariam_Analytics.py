"""
Project 3 Analytics Script

This script demonstrates skills in fetching data from the web, processing it using Python collections,
and writing the processed data to different file formats.

Author: Tesfamariam
Date: Jan. 26, 2024

"""

# Standard library imports
import csv
import pathlib 
import requests
from pathlib
import Path

# Function to fetch and write text data
def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
        write_txt_file(folder_name, filename, data)
    else:
        print(f"Failed to fetch data: {response.status_code}")

# Function to write text data to a file
def write_txt_file(folder_name, filename, data):
    file_path = Path(folder_name) / filename
    with open(file_path, 'w') as file:
        file.write(data)
    print(f"Text data saved to {file_path}")

# Function to fetch and write Excel data
def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.content
        write_excel_file(folder_name, filename, data)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

# Function to write Excel data to a file
def write_excel_file(folder_name, filename, data):
    file_path = Path(folder_name) / filename
    with open(file_path, 'wb') as file:
        file.write(data)
    print(f"Excel data saved to {file_path}")

# Main function to demonstrate functionality
def main():
    # Define URLs for data sources
    txt_url = 'https://www.cbssports.com/soccer/'
    excel_url = 'tutorial/samplefile.xlsx'

    # Define folder and file names
    txt_folder_name = 'data-txt'
    excel_folder_name = 'data-excel'
    txt_filename = 'sample.txt'
    excel_filename = 'sample.xlsx'

    # Fetch and write text data
    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)

    # Fetch and write Excel data
    fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url)

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
