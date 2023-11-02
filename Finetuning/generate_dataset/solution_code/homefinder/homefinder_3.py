from bs4 import BeautifulSoup
import csv

# Define the path to the HTML file
html_file = 'downloaded_pages/homefinder.html'

# Create a list to store the scraped data
scraped_data = []

# Open the HTML file and parse it using BeautifulSoup
with open(html_file, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

    # Find the div element containing the real estate agent's name
    name_div = soup.find(class_='cobrand-attribution-line1 mt-1')

    # Get the text of the real estate agent's name
    name = name_div.get_text(strip=True) if name_div else ""

    # Append the name to the scraped data list
    scraped_data.append({'Real Estate Agent Name': name})

# Define the path and filename for the CSV file
csv_file = 'scraped_data.csv'

# Write the scraped data to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Real Estate Agent Name'])
    writer.writeheader()
    writer.writerows(scraped_data)