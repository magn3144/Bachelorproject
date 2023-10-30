import csv
from lxml import etree

# Set up the file path and category
file_path = "downloaded_pages/woman.html"
category = "Blogs"

# Set up the XPaths for the elements
xpaths = [
    ("/html/body/div[6]/div[2]/div[3]/div/div/div[1]/div/div/span/a", "Klummer fra redaktionen"),
    ("/html/body/div[6]/div[2]/div[3]/div/div/div[2]/div[1]/div/span/a", "Klummer fra læserne"),
    ("/html/body/div[6]/div[2]/div[3]/div/div/div[3]/div[1]/div/span/a", "Blogs fra redaktionen"),
    ("/html/body/div[6]/div[2]/div[3]/div/div/div[4]/div[1]/div/span/a", "Blogs fra læserne"),
]

# Scrape the links from the web page
links = []
tree = etree.parse(file_path)
for xpath, label in xpaths:
    elements = tree.xpath(xpath)
    for element in elements:
        link = element.get("href")
        links.append([category, label, link])

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Category", "Label", "Link"])
    writer.writerows(links)