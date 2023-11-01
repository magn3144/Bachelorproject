import csv
from lxml import etree

# Define the local path to the HTML file
html_path = "downloaded_pages/ældresagen.html"

# Define the XPaths
cvr_xpath = "/html/body/div[2]/footer/section/div/div[1]/div[1]/div/p[4]"

# Read the HTML file
with open(html_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content
html_tree = etree.HTML(html_content)

# Extract the CVR number using XPath
cvr_element = html_tree.xpath(cvr_xpath)[0]
cvr_number = cvr_element.text

# Save the scraped data as CSV
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["CVR Number"])
    writer.writerow([cvr_number])