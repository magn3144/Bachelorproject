import os
import csv
from bs4 import BeautifulSoup

# Define the local path to the HTML file
html_path = "downloaded_pages/espn.html"

# Define the category
category = "Sports Websites"

# Define the target elements and their XPaths
elements = [
    {"xpath": "/html/body/div[1]/div/div/div/main/div[3]/div/div[1]/div[1]/div/section[2]/header/div[1]/h3", "name": "Date"},
    {"xpath": "/html/body/div[1]/div/div/div/main/div[3]/div/div[1]/div[1]/div/section[3]/div/section/div[1]/div/div[2]/a/h1", "name": "Headline"},
]

# Parse the HTML file
with open(html_path, "r") as file:
    html = file.read()
soup = BeautifulSoup(html, "html.parser")

# Scrape the data from the target elements
data = []
for element in elements:
    xpath = element["xpath"]
    name = element["name"]
    element = soup.find("xpath", xpath)
    if element:
        value = element.get_text(strip=True)
    else:
        value = ""
    data.append({name: value})

# Save the scraped data as a CSV file
output_path = "scraped_data.csv"
with open(output_path, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)