import csv
from lxml import etree

# Load the HTML file
html_path = "downloaded_pages/dst.html"
with open(html_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.parse(html_path, parser)

# Find the next update date element
next_update_element = tree.xpath("/html/body/div[1]/main/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[3]/div/div[4]")[0]

# Get the text of the next update date element
next_update_date = next_update_element.text.strip()

# Save the next update date as a CSV file
csv_path = "scraped_data.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Next Update Date"])
    writer.writerow([next_update_date])