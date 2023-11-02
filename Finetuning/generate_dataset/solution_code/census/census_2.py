import csv
from lxml import etree

# Define the HTML file path
html_file = 'downloaded_pages/census.html'

# Define the XPaths
xpaths = {
    'search_placeholder': '/html/body/div[3]/div/div/div[3]/header/div[1]/div[2]/div[2]/div[2]/span'
}

# Function to extract data from HTML using xpath
def extract_data(html, xpath):
    parser = etree.HTMLParser()
    tree = etree.parse(html, parser)
    element = tree.xpath(xpath)
    if element:
        return element[0].text.strip()
    else:
        return ''

# Extract the search_placeholder
search_placeholder = extract_data(html_file, xpaths['search_placeholder'])

# Save the scraped data as CSV file
data = [{'search_placeholder': search_placeholder}]

with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['search_placeholder'])
    writer.writeheader()
    writer.writerows(data)