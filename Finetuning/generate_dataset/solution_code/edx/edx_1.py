import csv
from pathlib import Path
from lxml import etree

# Read the HTML file
html_file = Path("downloaded_pages/edx.html")
with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

# Create an HTML parser
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Find the "see more Courses" link
link_element = tree.xpath('//a[contains(@class, "footer-seo-link text-info-500") and contains(text(),"see more Courses")]')
link_text = link_element[0].text if link_element else None

# Save the link text as CSV
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Link Text'])
    writer.writerow([link_text])