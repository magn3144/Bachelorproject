import csv
from lxml import html

# Load the webpage
with open("downloaded_pages/DTU_entrepreneurship.html", 'r') as f:
    webpage = f.read()

tree = html.fromstring(webpage)

# Get header and description
header = tree.xpath('/html/body/form/div[3]/footer/div[1]/div/div[2]/h2')[0].text
description = tree.xpath('/html/body/form/div[3]/div[5]/div[2]/div/div[2]/div/p')[0].text

# Save data to CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow([header, description])