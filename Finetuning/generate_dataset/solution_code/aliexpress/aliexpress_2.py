import csv
from lxml import etree

# Load the HTML file
with open('downloaded_pages/aliexpress.html', 'r') as file:
    html = file.read()

# Parse the HTML
root = etree.HTML(html)

# Find the welcome deal element
welcome_deal_element = root.xpath('//span[@class="tag--text--2VtIxqd tag--textStyle--vcAi3Rh"]')[0]

# Get the text of the welcome deal
welcome_deal_text = welcome_deal_element.text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Welcome Deal'])
    writer.writerow([welcome_deal_text])