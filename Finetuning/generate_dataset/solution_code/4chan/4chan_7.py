import csv
from lxml import etree

# Define the local path to the HTML file
html_path = 'downloaded_pages/4chan.html'

# Create a list to store the scraped URLs
urls = []

# Load the HTML file
with open(html_path, 'r') as file:
    html_content = file.read()

# Create an element tree from the HTML content
tree = etree.HTML(html_content)

# Find all the URLs for enabling mobile view and desktop site
mobile_view_urls = tree.xpath('//a[contains(text(), "Enable Mobile View")]/@href')
desktop_site_urls = tree.xpath('//a[contains(text(), "Disable Mobile View")]/@href')

# Add the URLs to the list
urls.extend(mobile_view_urls)
urls.extend(desktop_site_urls)

# Save the scraped URLs as a CSV file
with open('scraped_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['URL'])
    writer.writerows([[url] for url in urls])