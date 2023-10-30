import csv
from lxml import etree

# Read the HTML file
path = "downloaded_pages/wordpress.html"
with open(path, "r") as file:
    html_content = file.read()

# Parse the HTML
root = etree.HTML(html_content)

# Extract the title element
title_xpath = "/html/head/title"
title_element = root.xpath(title_xpath)[0]
title = title_element.text

# Save the title as CSV
csv_path = "scraped_data.csv"
with open(csv_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Title"])
    writer.writerow([title])