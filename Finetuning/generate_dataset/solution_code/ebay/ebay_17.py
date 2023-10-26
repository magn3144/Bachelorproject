import csv
from lxml import etree

# Define the target HTML file path
html_file_path = 'downloaded_pages/ebay.html'

# Define the XPaths for the HTML elements
condition_xpath = '/html/body/div[4]/div[3]/div[1]/div/div/div/ul[2]/li[3]/div/h3'

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file_path, parser)

# Find the condition element using XPath
condition_element = tree.xpath(condition_xpath)[0]

# Extract the condition text
condition = condition_element.text.strip() if condition_element is not None else ''

# Prepare the data for CSV
data = [{'Condition': condition}]

# Define the CSV file path
csv_file_path = 'scraped_data.csv'

# Write the data to CSV file
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Condition'])
    writer.writeheader()
    writer.writerows(data)