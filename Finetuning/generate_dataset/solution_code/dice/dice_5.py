import csv
from lxml import etree

# Load the HTML file
parser = etree.HTMLParser()
tree = etree.parse("downloaded_pages/dice.html", parser)

# Find all job URLs
job_urls = tree.xpath('//a[contains(@class, "card-title-link")]/@href')

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Job URL"])
    for url in job_urls:
        writer.writerow([url])