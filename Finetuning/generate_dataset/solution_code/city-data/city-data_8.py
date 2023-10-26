import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/city-data.html', 'r') as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Extract the text from the specified span element using XPath
span_element = tree.xpath('/html/body/div[3]/div[4]/div[2]/div/div[1]/div[1]/span')[0]
text = span_element.text.strip()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([text])