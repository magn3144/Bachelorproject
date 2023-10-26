import csv
from lxml import etree

# Load the HTML file
html = etree.parse('downloaded_pages/bbc.html', etree.HTMLParser())

# Find all elements with the specified class
titles = html.xpath('//span[contains(@class,"gs-c-promo-heading__title")]/text()')

# Filter titles that contain the keyword
filtered_titles = [title for title in titles if "Boats collide" in title]

# Save the filtered titles as CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title"])
    writer.writerows([[title] for title in filtered_titles])