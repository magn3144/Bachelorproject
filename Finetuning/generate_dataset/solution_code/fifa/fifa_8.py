import csv
from lxml import etree

# Define the HTML elements and their XPaths
elements = {
    "Homepage Link": "/html/body/div/div/div[1]/header/div[1]/nav/div[1]/a"
}

# Define the target web page
path = "downloaded_pages/fifa.html"

# Create an empty dictionary to store the scraped data
scraped_data = {}

# Open the HTML file and create an lxml etree
with open(path, "r", encoding="utf-8") as file:
    html = file.read()
    tree = etree.HTML(html)

# Scrape the data for each element
for key, value in elements.items():
    element = tree.xpath(value)
    if element:
        scraped_data[key] = element[0].text.strip()
    else:
        scraped_data[key] = ""

# Write the scraped data to a CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(scraped_data.keys())
    writer.writerow(scraped_data.values())