import csv
from lxml import html

# Define the target HTML file path
html_path = "downloaded_pages/google news.html"

# Define the XPaths for the div tags with class "vr1PYe"
xpaths = [
    "/html/body/c-wiz/div/div[2]/main/div[2]/c-wiz/section/div[3]/div/div[3]/c-wiz/c-wiz/div/div/article[3]/div[2]/div[1]/div/div",
    "/html/body/c-wiz/div/div[2]/main/div[2]/c-wiz/section/div[3]/div/div[3]/c-wiz/c-wiz/div/article/h4"
]

# Open the HTML file and parse it
with open(html_path, "r", encoding="utf-8") as file:
    html_content = file.read()
tree = html.fromstring(html_content)

# Scrape the text and corresponding XPaths of the div tags
scraped_data = []
for xpath in xpaths:
    elements = tree.xpath(xpath)
    for element in elements:
        text = element.text_content()
        scraped_data.append({"Text": text, "XPath": xpath})

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Text", "XPath"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(scraped_data)