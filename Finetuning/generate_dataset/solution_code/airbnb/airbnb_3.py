import csv
from scrapy import Selector

# Load the HTML file
with open('downloaded_pages/airbnb.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
selector = Selector(text=html_content)

# Find the grand pianos element
grand_pianos_element = selector.xpath('//span[contains(text(), "Grand pianos")]')

# Check if grand pianos element exists
if grand_pianos_element:
    grand_pianos_text = grand_pianos_element[0].xpath('string()').get().strip()
else:
    grand_pianos_text = ''

# Save the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([grand_pianos_text])