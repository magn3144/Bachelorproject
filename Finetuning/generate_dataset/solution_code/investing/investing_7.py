import csv
from lxml import etree

# Define the XPath expressions for the indices
indices_xpath = "/html/body/div/div[2]/div/div/div/main/div[6]/div[1]/div/div/table/tbody/tr/td[4]/div[1]/a/div"

# Read the HTML file
with open('downloaded_pages/investing.html', 'r') as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Find all the indices
indices_elements = tree.xpath(indices_xpath)

# Extract the names of the indices
indices_names = [element.text.strip() for element in indices_elements]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Index Name'])
    writer.writerows([[name] for name in indices_names])