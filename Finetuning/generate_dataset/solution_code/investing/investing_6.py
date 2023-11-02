# Import required libraries
import csv
from lxml import etree

# Define the path to the HTML file
html_file = 'downloaded_pages/investing.html'

# Load the HTML file
with open(html_file, 'r') as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.HTML(html, parser)

# Find all the currency pairs
currency_pairs = tree.xpath("//a[contains(@class, 'inv-link') and contains(@class, 'text-xs') and contains(@class, 'desktop:font-bold')]")
currency_pair_names = [pair.text for pair in currency_pairs]

# Save the currency pair names as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Currency Pair'])
    writer.writerows([[name] for name in currency_pair_names])