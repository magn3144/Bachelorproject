import csv
from lxml import etree

# Define the XPath expression for the desired element
xpath_expression = '/html/body/div/div[3]/div[5]/div/div/div[1]/div[2]/h6'

# Parse the HTML file
with open('downloaded_pages/globestudios.html', 'r') as file:
    tree = etree.parse(file)

# Find the desired element using XPath
element = tree.xpath(xpath_expression)[0]

# Extract the text from the element
text = element.text

# Save the extracted text as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([text])