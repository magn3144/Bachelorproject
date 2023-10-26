import requests
from lxml import etree
import csv

# Load the HTML file
with open("downloaded_pages/accuweather.html", "r") as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Find the RealFeel® and RealFeel Shade™ elements
realfeel_elements = tree.xpath("//span[contains(., 'RealFeel')]")

# Scrape the temperature information
temperatures = []
for element in realfeel_elements:
    temperature = element.text.strip()
    temperatures.append(temperature)

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["RealFeel Temperature"])
    writer.writerows(zip(temperatures))