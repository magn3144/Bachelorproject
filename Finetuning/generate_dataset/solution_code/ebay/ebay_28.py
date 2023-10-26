import csv
from bs4 import BeautifulSoup

# Load the HTML file
with open("downloaded_pages/ebay.html", "r") as f:
    html = f.read()

# Parse the HTML
soup = BeautifulSoup(html, "html.parser")

# Find the element with text "United States"
element = soup.find(text="United States")

# Get the text value
text = element.strip() if element else ""

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Country"])
    writer.writerow([text])