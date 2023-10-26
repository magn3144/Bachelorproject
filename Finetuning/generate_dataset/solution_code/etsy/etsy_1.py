import csv
from lxml import etree

# Define the XPath expressions for the advertisement elements
xpath_expressions = [
    "/html/body/main/div/div[1]/div/div[3]/div[2]/div[2]/div[7]/div/div/div/ol/li/div/div/a/div[2]/p/span/span",
    "/html/body/main/div/div[1]/div/div[3]/div[2]/div[2]/div[7]/div/div/div/ol/li/div/div/a/div[2]/p/span[1]/span",
    "/html/body/main/div/div[1]/div/div[3]/div[2]/div[2]/div[7]/div/div/div/ol/li/div/div/a/div[2]/p/span[2]/span"
]

# Parse the HTML file
html_parser = etree.HTMLParser()
tree = etree.parse("downloaded_pages/etsy.html", html_parser)

# Extract the advertisement texts using XPath expressions
ad_texts = []
for xpath_expr in xpath_expressions:
    elements = tree.xpath(xpath_expr)
    ad_texts += [element.text.strip() for element in elements if element.text]

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Advertisement Text"])
    writer.writerows([[ad_text] for ad_text in ad_texts])