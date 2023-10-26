import csv
from lxml import etree

# Define the XPaths for the specific elements
buying_format_xpath = "/html/body/div[4]/div[3]/div[1]/div/div/div/ul[2]/li[5]/div/h3"

# Load the HTML file
with open('downloaded_pages/ebay.html', 'r') as file:
    html_text = file.read()

# Create an ElementTree from the HTML text
tree = etree.HTML(html_text)

# Extract the buying format
buying_format_element = tree.xpath(buying_format_xpath)[0]
buying_format = buying_format_element.text.strip()

# Write the buying format to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Buying Format'])
    writer.writerow([buying_format])