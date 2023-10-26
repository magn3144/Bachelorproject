import csv
from lxml import etree
import os

def extract_text(element):
    return element.text.strip()

def extract_xpath(xpath):
    try:
        return root.xpath(xpath)[0]
    except IndexError:
        return None

category = "E-commerce"
target_page = "ebay"
local_path = "downloaded_pages/ebay.html"
task = "Retrieve the text 'Side Refine Panel'"

dom = etree.parse(local_path)
root = dom.getroot()

xpaths = {
    "Side Refine Panel": "/html/body/div[4]/div[3]/div[1]/div/header/h2"
}

scraped_data = {}

for key, xpath in xpaths.items():
    element = extract_xpath(xpath)
    if element is not None:
        scraped_data[key] = extract_text(element)

output_path = "scraped_data.csv"
with open(output_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Target Page", "Task", "Text"])
    writer.writerow([category, target_page, task, scraped_data.get("Side Refine Panel", "")])

print("Scraping completed and data saved successfully!")