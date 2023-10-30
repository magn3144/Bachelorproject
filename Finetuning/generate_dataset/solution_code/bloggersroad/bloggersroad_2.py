import csv
from lxml import html

# Define the local path to the HTML file
html_file = "downloaded_pages/bloggersroad.html"

# Read the HTML file
with open(html_file, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Retrieve the website's description using its XPath
description_xpath = "/html/head/meta[@name='description']/@content"
description = tree.xpath(description_xpath)

# Retrieve the website's XPath
xpath_xpath = "/html/head/meta[@name='description']/@data-xpath"
xpath = tree.xpath(xpath_xpath)

# Store the scraped data in a CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Description", "XPath"])
    writer.writerow([description, xpath])