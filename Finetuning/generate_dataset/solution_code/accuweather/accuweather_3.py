import csv
from lxml import etree

# Define the HTML file path
html_file_path = "downloaded_pages/accuweather.html"

# Define the XPaths for the title
title_xpath = "/html/head/title"

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file_path, parser)

# Extract the title
title = tree.xpath(title_xpath)[0].text

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Title"])
    writer.writerow([title])