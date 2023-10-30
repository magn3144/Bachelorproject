import csv
from lxml import etree

# Define the XPaths for the target elements
xpaths = {
    "search_text": "/html/body/div/div[1]/header/nav[2]/div/div/div/div/form/label"
}

# Load the HTML file
html_file = "downloaded_pages/wordpress.html"
with open(html_file, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.parse(html_content, parser)

# Extract the text from the target element
search_text = tree.xpath(xpaths["search_text"])[0].text

# Save the scraped data as a CSV file
csv_file = "scraped_data.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Search Text"])
    writer.writerow([search_text])