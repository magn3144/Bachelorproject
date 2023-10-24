import csv
from pathlib import Path
from lxml import etree

# Read the HTML file
file_path = Path("downloaded_pages/reddit.html")
with open(file_path, "r") as file:
    html_data = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html_data, parser)

# Scrape subreddit names
subreddit_names = tree.xpath("//a[@class='_3t5uN8xUmg0TOwRCOGQEcU']/text()")

# Save the scraped data to CSV
output_path = "scraped_data.csv"
with open(output_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subreddit"])
    writer.writerows([[name] for name in subreddit_names])