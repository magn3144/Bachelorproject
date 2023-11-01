import csv
from lxml import html

# Configuration
category = "Digital Websites"
local_path = "downloaded_pages/textures.html"
csv_file = "scraped_data.csv"

# Extract texture resolution information
tree = html.parse(local_path)
resolutions = tree.xpath('//div[@class="texture-res"]/text()')

# Save the scraped data as a CSV file
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Texture Resolution"])
    for resolution in resolutions:
        writer.writerow([category, resolution])