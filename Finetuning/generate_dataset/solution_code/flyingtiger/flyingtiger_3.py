import csv
from lxml import etree

# Load the HTML file
html_file = 'downloaded_pages/flyingtiger.html'
with open(html_file, 'r') as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Scrape the text inside all <p> tags
p_elements = tree.xpath('//p')
scraped_data = [p.text.strip() for p in p_elements]

# Save the scraped data as a CSV file
csv_file = 'scraped_data.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Text'])
    writer.writerows([[data] for data in scraped_data])