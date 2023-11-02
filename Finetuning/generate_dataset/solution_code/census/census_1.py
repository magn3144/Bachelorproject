import csv
from lxml import etree

# Define the target page URL and local path to the HTML file
url = 'https://example.com'  # Replace with the actual URL of the web page
html_file_path = 'downloaded_pages/census.html'  # Replace with the actual path to the HTML file

# Load the HTML file
with open(html_file_path, 'r') as file:
    html_content = file.read()

# Parse the HTML content
parser = etree.HTMLParser()
tree = etree.fromstring(html_content, parser)

# Define the xpath for the support text element
support_xpath = '/html/body/div[3]/div/div/div[11]/footer/div/div[2]/div[1]/div[1]/div[2]/div/a[2]/p'

# Find the support text element
support_element = tree.xpath(support_xpath)[0]

# Get the text of the support element
support_text = support_element.text.strip()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Support Text'])
    writer.writerow([support_text])