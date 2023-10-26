import csv
from bs4 import BeautifulSoup

html_file = 'downloaded_pages/ebay.html'
xpath = '/html/body/div[4]/div[4]/div[3]/section/div[1]/div[2]/div[1]/div/div/form/div[1]/div/span/div/div[65]/span'

# Function to extract the text using XPath
def extract_text(element):
    return element.get_text(strip=True)

# Parse the HTML file
with open(html_file, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find the element using XPath
element = soup.find(xpath)

# Extract the text from the element
text = extract_text(element)

# Write the text to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Scraped Data'])
    writer.writerow([text])