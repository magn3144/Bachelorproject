import csv
from lxml import etree

# Load HTML file
html_file = 'downloaded_pages/airbnb.html'
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Define XPaths for guest favorites
guest_favorites_xpaths = [
    '/html/body/div[5]/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/h1/div[3]/a/span',
    '/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[24]/div/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div',
    '/html/body/div[5]/div/div/div[1]/div/div[2]/main/div[2]/div/div/div/div/div[1]/div[7]/div/div[2]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div'
]

# Scrape guest favorites
guest_favorites = []
for xpath in guest_favorites_xpaths:
    element = tree.xpath(xpath)
    if element:
        guest_favorites.append(element[0].text.strip())
    else:
        guest_favorites.append(None)

# Save scraped data as CSV
data = {'Guest Favorites': guest_favorites}
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data.keys())
    writer.writeheader()
    writer.writerow(data)