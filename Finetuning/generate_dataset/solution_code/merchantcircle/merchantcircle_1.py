import csv
from scrapy import Selector

# Load the HTML file
with open('downloaded_pages/merchantcircle.html') as file:
    html = file.read()

# Create a selector object
sel = Selector(text=html)

# Get the category names
category_names = sel.xpath('//h2/a/text()').extract()

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category Name'])
    writer.writerows(zip(category_names))