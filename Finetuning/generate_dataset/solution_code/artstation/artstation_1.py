import csv
from lxml import etree

# Define XPath expressions for the marketplace sale titles
title_xpath = "/html/body/div[1]/div[1]/a/span[1]"

# Read the HTML file
with open('downloaded_pages/artstation.html', 'r') as file:
    html_str = file.read()

# Parse the HTML
doc = etree.HTML(html_str)

# Extract the marketplace sale titles
titles = doc.xpath(title_xpath)

# Save the titles to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Marketplace Sale Title"])
    for title in titles:
        writer.writerow([title.text])