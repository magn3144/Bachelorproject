import csv
from pathlib import Path
from bs4 import BeautifulSoup

# Set the local path to the HTML file
html_file = Path("downloaded_pages/nytimes.html")

# Read the HTML file
with open(html_file, "r") as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Scrape the titles of the articles in the "Energy Agency" section
article_titles = []
energy_agency_section = soup.find("section", class_="css-1nu0qi8 e199n1pr0")
if energy_agency_section:
    article_links = energy_agency_section.find_all("a", class_="css-1u3p7j1")
    for link in article_links:
        article_titles.append(link.text.strip())

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Article Title"])
    for title in article_titles:
        writer.writerow([title])