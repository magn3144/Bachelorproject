import csv
from lxml import etree

# Load the HTML page
html_path = 'downloaded_pages/airbnb.html'
with open(html_path, 'r') as f:
    html_text = f.read()

# Parse the HTML
html_tree = etree.HTML(html_text)

# Function to retrieve text content using XPath
def get_text(xpath):
    elements = html_tree.xpath(xpath)
    if len(elements) > 0:
        return elements[0].text.strip()
    else:
        return ''

# Collect information about Nykøbing Sjælland, Denmark
title_xpath = '/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[35]/div/div[2]/div/div/div/div/div/div[2]/div[1]'
title = get_text(title_xpath)

# Store the scraped data as CSV
data = [['Title', 'Category']]
data.append([title, 'Tourism'])

csv_path = 'scraped_data.csv'
with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)