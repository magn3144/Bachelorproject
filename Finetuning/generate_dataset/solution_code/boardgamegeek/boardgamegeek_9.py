import csv
from lxml import etree

# Load HTML file
tree = etree.parse("downloaded_pages/boardgamegeek.html")
root = tree.getroot()

# XPaths for game-specific forums
xpaths = [
    "/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/div/gg-forum-listings/gg-forum-section-list[10]/section/ul/li[*]/gg-forum-listing/div/div[2]/div/a[5]",
    "/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/div/gg-forum-listings/gg-forum-section-list[10]/section/ul/li[*]/gg-forum-listing/div/div[2]/div/a[6]"
]

# Scrape names and descriptions of game-specific forums
data = []
for xpath in xpaths:
    elements = root.xpath(xpath)
    for element in elements:
        name = element.text.strip()
        description = element.getparent().getparent().find(".//p/span").text.strip()
        data.append({"Name": name, "Description": description})

# Save scraped data as CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Name", "Description"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)