import csv
from lxml import etree

# Define the target HTML file path
html_file = 'downloaded_pages/ebay.html'

# Define the XPaths for the HTML elements
bids_offers_link_xpath = '/html/body/div[3]/header/div/ul[2]/li[4]/div/div/ul/li[3]/a'

# Define the category and task
category = 'E-commerce'
task = 'Extract the "Bids/Offers" link'

# Parse the HTML file
tree = etree.parse(html_file)

# Extract the "Bids/Offers" link
bids_offers_link = tree.xpath(bids_offers_link_xpath)[0].text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Category', 'Task', 'Bids/Offers Link'])
    writer.writerow([category, task, bids_offers_link])