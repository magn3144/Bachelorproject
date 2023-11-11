import csv
from pathlib import Path
from bs4 import BeautifulSoup

# Read the HTML file
html_file = Path("downloaded_pages/urbandictionary.html").read_text()

# Parse HTML
soup = BeautifulSoup(html_file, "html.parser")

# Find the "H" link using xpath
xpath = "/html/body/div/header/div[2]/div[1]/div/div/ul/li[1]/div/div/ul/li[8]/a"
h_link = soup.select_one(xpath)

# Get the text and XPath of the "H" link
h_text = h_link.text.strip()
h_xpath = xpath

# Save the scraped data as a CSV file
data = [[h_text, h_xpath]]
with open("scraped_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Text", "XPath"])
    writer.writerows(data)