import csv
from lxml import etree

# Define the HTML file path
html_file_path = "downloaded_pages/city-data.html"

# Define the XPath for the target element
target_xpath = "/html/body/div[3]/div[4]/div[2]/div/div[1]/div[1]/ul/li[1]"

# Parse the HTML file
html_parser = etree.HTMLParser()
tree = etree.parse(html_file_path, html_parser)

# Find the target element using XPath
target_element = tree.xpath(target_xpath)[0]

# Extract the text from the target element
target_text = target_element.text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([target_text])