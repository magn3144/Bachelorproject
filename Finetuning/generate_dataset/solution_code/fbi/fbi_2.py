import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/fbi.html', 'r') as f:
    html = f.read()

# Parse the HTML
doc = etree.HTML(html)

# Scrape the FBI email alerts description
fbi_email_alerts = doc.xpath('/html/body/section/div/div[2]/div/p/span[2]')[0].text

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['FBI Email Alerts Description'])
    writer.writerow([fbi_email_alerts])