from pathlib import Path
from bs4 import BeautifulSoup
import csv

# Define the URL, local file path, and category
url = "https://www.aljazeera.com"
file_path = "downloaded_pages/aljazeera.html"
category = "News"

# Read the HTML file
html_file = Path(file_path).read_text()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_file, "html.parser")

# Find all H2 headings
h2_headings = soup.find_all("h2")

# Store the headings in a CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Category", "Heading"])
    for heading in h2_headings:
        writer.writerow([category, heading.text])