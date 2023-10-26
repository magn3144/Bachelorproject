import csv
from lxml import etree

# Read the HTML file
with open("downloaded_pages/edx.html", "r") as file:
    html_data = file.read()

# Parse the HTML
tree = etree.HTML(html_data)

# Get the text of the "Boot Camps" div
boot_camps_div = tree.xpath('//div[@class="mx-auto"]/text()')[0]

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([boot_camps_div])