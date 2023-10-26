import csv
from lxml import html

# Define the category, local path, and XPath expression
category = "Sports Websites"
local_path = "downloaded_pages/cbsports.html"
xpath_expr = "//div[@class='h4 grid-view-item__title product-card__title']"

# Open the HTML file and parse it
with open(local_path, "r", encoding="utf-8") as file:
    content = file.read()
tree = html.fromstring(content)

# Find all div elements with the specified class using XPath
div_elements = tree.xpath(xpath_expr)

# Extract the text from the div elements
div_text = [div.text_content().strip() for div in div_elements]

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Text"])
    for text in div_text:
        writer.writerow([category, text])