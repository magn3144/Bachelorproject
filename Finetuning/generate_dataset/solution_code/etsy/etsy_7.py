import csv
from pathlib import Path
from lxml import etree

# Define the XPaths for the target elements
xpaths = {
    "question": "/html/body/main/div/div[8]/div/div/div[2]/div[2]/div/div[1]/h2"
}

# Define the local path to the HTML file
html_path = "downloaded_pages/etsy.html"

# Parse the HTML file
with open(html_path, "r") as file:
    html = file.read()
    parser = etree.HTMLParser()
    tree = etree.fromstring(html, parser)

# Extract the text content of the target elements using XPaths
question = tree.xpath(xpaths["question"])[0].text

# Save the scraped data as a CSV file
csv_path = Path("scraped_data.csv")
with csv_path.open(mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Question"])
    writer.writerow([question])

print(f"Scraped data has been saved as {csv_path}")