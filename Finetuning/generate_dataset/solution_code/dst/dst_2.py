import csv
from lxml import etree

# Load the HTML document
with open('downloaded_pages/dst.html', 'rb') as file:
    html = file.read()

# Parse the HTML document
tree = etree.HTML(html)

# Find and scrape the selected statistics on divorces
divorce_stats = tree.xpath("/html/body/div[1]/main/div/div[2]/div[1]/div/div/div[3]/div[2]/div")

# Extract the data from the selected statistics
data = []
for stat in divorce_stats:
    h2 = stat.xpath("./h2/text()")[0].strip()
    div = stat.xpath("./div/text()")[0].strip()
    data.append([h2, div])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)