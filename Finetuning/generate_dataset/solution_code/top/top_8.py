import csv
from lxml import etree

# Define the XPath expression for the <h6> element
xpath_expression = '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div/div[3]/div/div[2]/div/article/div[2]/a/h6'

# Load the HTML file
html_path = 'downloaded_pages/top.html'
with open(html_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
tree = etree.HTML(html_content)

# Find the <h6> element using the XPath expression
h6_element = tree.xpath(xpath_expression)[0]

# Get the text from the <h6> element
text = h6_element.text

# Save the text as CSV
csv_path = 'scraped_data.csv'
with open(csv_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([text])