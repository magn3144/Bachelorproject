import csv
from lxml import etree

# Define the XPath for the "Brand" element
brand_xpath = "/html/body/div[4]/div[3]/div[1]/div/div/div/ul[2]/li[1]/div/h3"

# Load the HTML file
html_file = "downloaded_pages/ebay.html"
with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

# Parse the HTML content
html = etree.HTML(html_content)

# Scrape the "Brand" text
brand_element = html.xpath(brand_xpath)
brand_text = brand_element[0].text.strip() if brand_element else ""

# Save the scraped data as a CSV file
data = [["Brand", brand_text]]
csv_file = "scraped_data.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)