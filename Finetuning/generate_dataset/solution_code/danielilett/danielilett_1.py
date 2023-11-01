import csv
from bs4 import BeautifulSoup

# Define the HTML file path
html_file_path = "downloaded_pages/danielilett.html"

# Load the HTML file
with open(html_file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Scrape link texts and their corresponding XPaths
link_texts = []
xpaths = []

for element in soup.find_all("a"):
    link_texts.append(element.text.strip())
    xpath = soup.find("a", text=element.text.strip()).xpath()
    xpaths.append(xpath)

# Save the scraped data as a CSV file
data = zip(link_texts, xpaths)

with open("scraped_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Link Text", "XPath"])
    writer.writerows(data)