import csv
from lxml import etree

# Define the target HTML file path
html_file_path = 'downloaded_pages/city-data.html'

# Define the XPath for the span element
span_xpath = '/html/body/div[3]/div[4]/div[4]/div/span'

# Parse the HTML file
tree = etree.parse(html_file_path)

# Find the span element using XPath
span_element = tree.xpath(span_xpath)[0]

# Get the text from the span element
span_text = span_element.text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([span_text])