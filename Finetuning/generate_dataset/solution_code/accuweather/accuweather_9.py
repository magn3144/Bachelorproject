import csv
from lxml import etree

# Read the HTML file
html_file = "./downloaded_pages/accuweather.html"
with open(html_file, "r", encoding="utf-8") as file:
    html_data = file.read()

# Parse the HTML
tree = etree.HTML(html_data)

# Scrape the index status phrase using the corresponding XPath
index_status_phrase = tree.xpath("/html/body/div/div[7]/div[1]/div[1]/div[2]/div[2]/div[3]/a[6]/div[5]/text()")[0]

# Save the scraped data as a CSV file
data = [["Index Status Phrase"]]
data.append([index_status_phrase])

with open('scraped_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)