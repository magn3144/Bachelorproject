import csv
from lxml import etree

# Load the HTML file
html_file = 'downloaded_pages/flyingtiger.html'
with open(html_file, 'r') as file:
    html_data = file.read()

# Parse the HTML
tree = etree.HTML(html_data)

# Scrape the text inside all <a> tags
a_elements = tree.xpath('//a')
scraped_data = [a.text.strip() for a in a_elements if a.text]

# Save the scraped data as a CSV file
csv_file = 'scraped_data.csv'
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Scraped Text'])
    writer.writerows(zip(scraped_data))