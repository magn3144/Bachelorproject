import csv
import os
from lxml import etree

# Define the XPath expressions for the dates of the article elements
xpath_dates = "/html/body/div/div/div[3]/div/div[3]/div/div[1]/section/article//span[contains(@class, 'screen-reader-text')]/text()"

# Parse the HTML file
html_file = os.path.join("downloaded_pages", "aljazeera.html")
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Extract the dates using XPath
dates = tree.xpath(xpath_dates)

# Create a list of dictionaries with the scraped data
records = [{'date': date} for date in dates]

# Define the path to save the CSV file
csv_file = "scraped_data.csv"

# Write the data to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['date'])
    writer.writeheader()
    writer.writerows(records)