import csv
from lxml import etree

# Read the HTML file
html_path = "downloaded_pages/top.html"
with open(html_path, "r") as file:
    html_content = file.read()

# Create an ElementTree object from the HTML content
tree = etree.HTML(html_content)

# Scrape the category of the website
category_element = tree.xpath("/html/body/div/div/div/div[1]/div[1]/div[2]/h1")[0]
category = category_element.text.strip()

# Save the scraped data as a CSV file
csv_path = "scraped_data.csv"
with open(csv_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Category"])
    writer.writerow([category])