import csv
from bs4 import BeautifulSoup

# Define the HTML file path
html_file = 'downloaded_pages/homefinder.html'

# Create a list to store the zip codes
zip_codes = []

# Open the HTML file and parse it with BeautifulSoup
with open(html_file, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

    # Find all the HTML elements containing zip codes
    zip_code_elements = soup.find_all('label', text="      Zip Codes in      New York, NY    ")

    # Extract the zip codes from the zip code elements
    for element in zip_code_elements:
        zip_code = element.next_sibling.strip()
        zip_codes.append(zip_code)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Zip Code'])
    writer.writerows(zip_codes)