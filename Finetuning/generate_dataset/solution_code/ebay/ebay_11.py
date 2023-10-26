import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/ebay.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
tree = etree.HTML(html_content)

# Find the User Agreement link
user_agreement_element = tree.xpath('//a[contains(text(), "User Agreement")]')[0]
user_agreement_link = user_agreement_element.get('href')

# Save the scraped data as a CSV file
data = [[user_agreement_link]]
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)