import csv
from lxml import html

# Define the XPaths for the target elements
xpaths = {
    "heading": "/html/body/div/main/div[1]/div[2]/div/section[4]/div[1]/h2"
}

# Parse the HTML file
with open('downloaded_pages/bog & ide.html', 'r', encoding="utf-8") as f:
    tree = html.fromstring(f.read())

# Scrape the heading text
heading_element = tree.xpath(xpaths["heading"])
heading_text = heading_element[0].text if len(heading_element) != 0 else ""

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Heading"])
    writer.writerow([heading_text])