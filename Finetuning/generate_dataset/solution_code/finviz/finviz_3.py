import csv
import requests
from lxml import html

# Define the category, local path, and URL
category = "Stocks"
local_path = "downloaded_pages/finviz.html"
url = "https://finviz.com"

# Load the HTML page
page = requests.get(url+"/"+local_path)
tree = html.fromstring(page.content)

# Scrape the sectors from the page
sectors = tree.xpath('//th[@class="table-header cursor-pointer" and text()="Sector"]/text()')

# Save the scraped data as CSV
with open("scraped_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Category", "Sector"])
    for sector in sectors:
        writer.writerow([category, sector])