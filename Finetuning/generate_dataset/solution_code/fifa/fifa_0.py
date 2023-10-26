import csv
from lxml import etree

# Read the HTML file
html_file = "downloaded_pages/fifa.html"
with open(html_file, "r") as f:
    html_data = f.read()

# Create an XML tree from the HTML data
parser = etree.HTMLParser()
tree = etree.fromstring(html_data, parser)

# Define the XPath expressions for the section titles
section_title_xpaths = [
    "/html/body/div/div/main/div/section/div/div[1]/div[1]/h1/span[2]/span",
    "/html/body/div/div/main/div/section/div/div[2]/div/div/div/div/div/h4/span[2]/span",
    "/html/body/div/div/main/div/section/div/div[2]/div[1]/div/h3/span[2]/span",
    "/html/body/div/div/main/div/section/div/div[2]/div[2]/div/div[1]/h4/span[2]/span",
    "/html/body/div/div/main/div/section/div/div[3]/div/div/div/div/h4/span[2]/span",
    "/html/body/div/div/main/div/section/div/div[4]/div[1]/div/h3/span[2]/span",
    "/html/body/div/div/main/div/section/div/div[4]/div[2]/div/div[1]/div/h4/span[2]/span"
]

# Scrape the section titles
section_titles = []
for xpath in section_title_xpaths:
    section_title = tree.xpath(xpath)
    if section_title:
        section_titles.append(section_title[0].text)
    else:
        section_titles.append("")

# Save the scraped data as CSV
output_file = "scraped_data.csv"
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Section", "Title"])
    for i, title in enumerate(section_titles):
        writer.writerow([f"Section {i+1}", title])