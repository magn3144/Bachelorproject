import csv
from lxml import etree

# Open the HTML file and create an ElementTree
tree = etree.parse("downloaded_pages/boardgamegeek.html")
root = tree.getroot()

# Find all the hotness items
hotness_items = root.xpath("//gg-hotness-items/ul/li")

# Create a list to store the extracted data
data = []

# Iterate over each hotness item
for item in hotness_items:
    # Extract the title and link
    title = item.xpath(".//h2/a")[0].text.strip()
    link = item.xpath(".//h2/a/@href")[0]

    # Append the data to the list
    data.append([title, link])

# Save the data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])
    writer.writerows(data)