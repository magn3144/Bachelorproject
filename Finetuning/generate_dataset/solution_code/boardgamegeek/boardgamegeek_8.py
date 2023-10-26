import csv
from lxml import etree

# Define the XPaths for the global stat elements
xpaths = {
    'total_threads': '/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/gg-forum-sidebar/div/div[3]/dl/div[1]/dd',
    'total_replies': '/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/gg-forum-sidebar/div/div[3]/dl/div[2]/dd',
    'total_thumbs': '/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/gg-forum-sidebar/div/div[3]/dl/div[3]/dd'
}

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse('downloaded_pages/boardgamegeek.html', parser)

# Scrape the global statistics using the defined XPaths
global_stats = {}
for key, value in xpaths.items():
    element = tree.xpath(value)
    if element:
        global_stats[key] = element[0].text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=global_stats.keys())
    writer.writeheader()
    writer.writerow(global_stats)