import csv
from lxml import etree

# Read the HTML file
html_file = "downloaded_pages/edx.html"

# Define the XPath for the target div
target_xpath = "/html/body/div[1]/div[1]/div/main/div/div[1]/div/div/div/div[2]"

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Find the target div using XPath
target_div = tree.xpath(target_xpath)[0]

# Get the text of the target div
target_text = target_div.text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Text'])
    writer.writerow([target_text])