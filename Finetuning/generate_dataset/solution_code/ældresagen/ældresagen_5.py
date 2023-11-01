import csv
from lxml import etree

# Define the XPath for the top layer element in the footer
xpath = "/html/body/div[2]/footer/section/div/div[1]/div[2]/div/div[2]"

# Parse the HTML file
tree = etree.parse('downloaded_pages/ældresagen.html')

# Find the top layer element using XPath
top_layer_element = tree.xpath(xpath)[0]

# Get the text from the top layer element
text = top_layer_element.text.strip()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([text])