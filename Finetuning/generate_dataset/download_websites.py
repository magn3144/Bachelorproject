import requests
import csv
import os
from bs4 import BeautifulSoup


def download_websites(CSV_name, save_folder):
    # Ensure to create a directory to save the HTML files
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Read websites from the CSV file
    with open(CSV_name, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        
        for row in reader:
            category, website, page, link = row
            
            try:
                # Make a GET request to fetch the raw HTML content
                response = requests.get(link, timeout=10)
                
                # Check if the request was successful (HTTP Status Code 200)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    # Save the HTML content to a file
                    with open(f'{save_folder}/{website}.html', 'w', encoding='utf-8') as html_file:
                        html_file.write(str(soup))
                    print(f"Downloaded {website}")
                else:
                    print(f"Failed to retrieve {website}")
            except Exception as e:
                print(f"Error retrieving {website}: {str(e)}")