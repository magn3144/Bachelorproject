import csv
import requests
from lxml import etree

# Define the target URL and local path to the HTML file
url = "https://www.etsy.com"
local_path = "downloaded_pages/etsy.html"

# Load the HTML content from the webpage or local file
try:
    with open(local_path, "r") as f:
        html_content = f.read()
except FileNotFoundError:
    response = requests.get(url)
    html_content = response.content

# Parse the HTML content
html_tree = etree.HTML(html_content)

# Retrieve all shop names using the given XPaths
xpaths = [
    "/html/body/main/div/div[3]/div/div/div",
    "/html/body/main/div/div[1]/div/div[3]/div[2]/div[2]/div[7]/div/div/div/ol/li[4]/div/div/a/div[2]/p/span[2]/span",
    "/html/body/main/div/div[1]/div/div[3]/div[2]/div[2]/div[7]/div/div/div/ol/li[28]/div/div/a/div[2]/p/span[4]",
    "/html/body/main/div/div[1]/div/div[3]/div[2]/div[2]/div[7]/div/div/div/ol/li[50]/div/div/a/div[2]/p/span[1]/span"
]

shop_names = []
for xpath in xpaths:
    elements = html_tree.xpath(xpath)
    for element in elements:
        shop_names.append(element.text)

# Save the scraped data as a CSV file
with open("scraped_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Shop Names"])
    writer.writerows([[name] for name in shop_names])