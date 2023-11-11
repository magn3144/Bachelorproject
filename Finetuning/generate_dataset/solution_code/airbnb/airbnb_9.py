import csv
from lxml import etree

# Define the XPaths for the elements to scrape
xpaths = {
    "emergency_stays": "/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[3]/div[2]/footer/div/div/div[1]/section[3]/ul/li[6]/a"
}

# Load the HTML file
html_file = "downloaded_pages/airbnb.html"
with open(html_file, "r") as f:
    html_content = f.read()

# Parse the HTML content
parser = etree.HTMLParser()
tree = etree.fromstring(html_content, parser)

# Scrape the emergency stays information
emergency_stays_element = tree.xpath(xpaths["emergency_stays"])[0]
emergency_stays = emergency_stays_element.text

# Write the scraped data to a CSV file
data = [["Category", "Emergency Stays"], ["Tourism", emergency_stays]]
csv_file = "scraped_data.csv"
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)