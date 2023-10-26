import csv
from lxml import etree

# Define the file path
file_path = "downloaded_pages/boardgamegeek.html"

# Define the XPaths for replies and thumbs
xpaths = [
    "/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/div/gg-forum-listings/gg-forum-section-list[10]/section/ul/li[3]/gg-forum-listing/div/div[1]/dl/div[2]/dd",
    "/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/div/gg-forum-listings/gg-forum-section-list[10]/section/ul/li[3]/gg-forum-listing/div/div[1]/dl/div[3]/dd"
]

# Scrape the data
data = []
tree = etree.parse(file_path)
for xpath in xpaths:
    elements = tree.xpath(xpath)
    if elements:
        replies = elements[0].text.strip()
        thumbs = elements[1].text.strip()
        data.append([replies, thumbs])

# Save the data as a CSV file
with open('scraped_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Replies', 'Thumbs'])
    writer.writerows(data)