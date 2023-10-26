import csv
from lxml import etree

# Define the XPath expressions for the target elements
xpath_expressions = {
    "source_attribute": "/html/body/div/div[7]/div[1]/div[1]/div[2]/div[3]",
}

# Load the HTML file
html_file = "downloaded_pages/accuweather.html"
with open(html_file, "r", encoding="utf-8") as file:
    html_data = file.read()

# Parse the HTML and create the ElementTree
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Scrape the source attribute information
source_attribute = tree.xpath(xpath_expressions["source_attribute"])[0].text

# Save the scraped data as a CSV file
data = [["Source Attribute"]]
data.append([source_attribute])

output_file = "scraped_data.csv"
with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Scraping completed and data saved successfully.")