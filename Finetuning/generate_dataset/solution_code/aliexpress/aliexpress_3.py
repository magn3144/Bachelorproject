import csv
from lxml import etree

# Define the paths to the HTML file and the CSV file
html_path = 'downloaded_pages/aliexpress.html'
csv_path = 'scraped_data.csv'

# Define the XPath for the global GDPR message
gdpr_xpath = '/html/body/div[10]/div/div[1]'

# Parse the HTML file using lxml's etree
tree = etree.parse(html_path)

# Find the global GDPR message using the XPath
gdpr_element = tree.xpath(gdpr_xpath)[0]

# Get the text content of the GDPR element
gdpr_text = gdpr_element.text.strip()

# Save the scraped data as a CSV file
with open(csv_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['GDPR Message'])
    writer.writerow([gdpr_text])