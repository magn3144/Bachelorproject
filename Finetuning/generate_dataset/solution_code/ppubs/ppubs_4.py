import csv
from lxml import etree

# Load HTML file
html_file = "downloaded_pages/ppubs.html"
with open(html_file, "r") as f:
    html_data = f.read()

# Define the list of labels and their corresponding XPaths
labels = [
    ("Patent or Publication number", "/html/body/div[2]/div/section[1]/div/div[1]/div/div[2]/div/div/form/div/label"),
    ("Operator", "/html/body/div[2]/div/section[1]/div/div[1]/div/div[4]/div/div/form/div[2]/div/div/label"),
    ("For", "/html/body/div[2]/div/section[1]/div/div[1]/div/div[4]/div/div/form/div[1]/div[2]/div/label"),
    ("Search", "/html/body/div[2]/div/section[1]/div/div[1]/div/div[4]/div/div/form/div[1]/div[1]/div/label"),
    ("For", "/html/body/div[2]/div/section[1]/div/div[1]/div/div[4]/div/div/form/div[3]/div[2]/div/label"),
    ("Publication date", "/html/body/div[2]/div/section[2]/div/div/div/div/div[2]/div/table/thead/tr/th[6]")
]

# Scrape the text enclosed by the <label> tags using XPaths
scraped_data = []
dom = etree.HTML(html_data)
for label, xpath_expr in labels:
    elements = dom.xpath(xpath_expr)
    if elements:
        text = elements[0].text.strip() if elements[0].text else ""
        scraped_data.append((label, text))

# Save the scraped data to a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Label", "Text"])
    writer.writerows(scraped_data)