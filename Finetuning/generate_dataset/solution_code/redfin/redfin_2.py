import csv
import os
from lxml import etree

# Define the file paths
html_file_path = 'downloaded_pages/redfin.html'
csv_file_path = 'scraped_data.csv'

# Load the HTML file
with open(html_file_path, 'r') as html_file:
    html_content = html_file.read()

# Parse the HTML content
parser = etree.HTMLParser()
tree = etree.HTML(html_content)

# Extract all the listed home prices
home_price_elements = tree.xpath('//div[contains(@class, "column_3 col_price")]')
home_prices = [element.text.strip() for element in home_price_elements]

# Save the scraped data as a CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Home Price'])
    writer.writerows(zip(home_prices))

# Print the success message
print('Scraping complete. Data saved in scraped_data.csv.')