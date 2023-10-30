import csv
from lxml import etree

# Define the local path to the HTML file
html_file = 'downloaded_pages/bog & ide.html'

# Define the XPath of the element to be scraped
xpath = '/html/body/div/main/div[1]/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/div/div/h2/a'

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Find the element using XPath
element = tree.xpath(xpath)[0]

# Get the text from the element
text = element.text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([text])