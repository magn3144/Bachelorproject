import csv
from lxml import etree

# Define the HTML file path
html_file = "downloaded_pages/bloggersroad.html"

# Define the XPaths for the menu items
menu_item_xpaths = [
    ("/html/body/div/header/div[2]/div/div/nav/ul/li[1]/a", "Home"),
    ("/html/body/div/header/div[2]/div/div/nav/ul/li[2]/a", "Business"),
    ("/html/body/div/header/div[2]/div/div/nav/ul/li[3]/a", "Fashion"),
    ("/html/body/div/header/div[2]/div/div/nav/ul/li[4]/a", "Shopping"),
    ("/html/body/div/header/div[2]/div/div/nav/ul/li[5]/a", "Pets"),
]

# Create a list to store the scraped data
scraped_data = []

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Scrape the menu items using the XPaths
for xpath, menu_name in menu_item_xpaths:
    elements = tree.xpath(xpath)
    if elements:
        menu_item = {
            "Menu Name": menu_name,
            "XPath": xpath,
        }
        scraped_data.append(menu_item)

# Save the scraped data as a CSV file
with open("scraped_data.csv", mode="w", newline="") as file:
    fieldnames = ["Menu Name", "XPath"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(scraped_data)