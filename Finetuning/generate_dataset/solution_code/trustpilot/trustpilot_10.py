import csv
from lxml import etree

# Load the HTML file
with open('downloaded_pages/trustpilot.html', 'r') as file:
    html = file.read()

# Create an XML tree from the HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Find the footer element
footer_element = tree.xpath('/html/body/div/div/div/footer')[0]

# Find all the support center names
support_center_elements = footer_element.xpath('.//a[contains(@class, "footer-link_footerLink")]/text()')
support_center_names = [element.strip() for element in support_center_elements]

# Save the support center names as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Support Center Name'])
    writer.writerows([[name] for name in support_center_names])