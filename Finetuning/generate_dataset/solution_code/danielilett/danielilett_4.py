import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open("downloaded_pages/danielilett.html", "r") as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, "html.parser")

# Find all div elements
divs = soup.find_all("div")

# Create a list to store scraped data
scraped_data = []

# Iterate over the div elements and extract text and xpath
for div in divs:
    text = div.text.strip()
    xpath = soup.find(string=text).find_parents()[0].findPreviousSiblings(recursive=False).index(div) + 1
    scraped_data.append([text, xpath])

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(scraped_data)