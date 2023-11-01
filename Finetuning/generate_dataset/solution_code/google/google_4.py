import csv
from lxml import etree

# Load HTML file
html_file = 'downloaded_pages/google.html'
with open(html_file, 'r') as f:
    html = f.read()

# Parse HTML
tree = etree.HTML(html)

# Scrape the title of the Doodle with the "Celebrating Papeda" heading
xpath = '/html/body/div[2]/div/ul/li[1]/div/h2'
title = tree.xpath(xpath)[0].text.strip()

# Save the scraped data as a CSV file
data = [['Title']]
data.append([title])

csv_file = 'scraped_data.csv'
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)