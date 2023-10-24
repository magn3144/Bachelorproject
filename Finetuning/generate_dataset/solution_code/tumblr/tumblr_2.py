import csv
from lxml import etree

# Define the HTML file path
html_file = "downloaded_pages/tumblr.html"

# Define the XPaths
xpaths = {
    "hashtags": "//span[contains(@class, 'SLpX8')]/text()",
}

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Find all the hashtags
hashtags = tree.xpath(xpaths["hashtags"])

# Prepare the data for CSV
data = [{"hashtag": hashtag} for hashtag in hashtags]

# Save the data to a CSV file
with open("scraped_data.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["hashtag"])
    writer.writeheader()
    writer.writerows(data)