import csv
from lxml import etree

# Define the target HTML file path
html_path = 'downloaded_pages/boardgamegeek.html'

# Define the XPaths for the privacy options details
xpath_privacy_options = '/html/body/div[3]/div/div[1]/div/div[1]'

# Parse the HTML file
with open(html_path, 'r') as html_file:
    html = html_file.read()
    tree = etree.HTML(html)

# Extract the privacy options details using the XPath
privacy_options_elements = tree.xpath(xpath_privacy_options)
privacy_options_details = [elem.text.strip() for elem in privacy_options_elements]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Privacy Options Details"])
    writer.writerow(privacy_options_details)