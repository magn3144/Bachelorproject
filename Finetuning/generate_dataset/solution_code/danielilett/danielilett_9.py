import csv
from lxml import etree

# Load the HTML file
html_file = 'downloaded_pages/danielilett.html'
with open(html_file, 'r') as f:
    html_data = f.read()

# Create an HTML parser
parser = etree.HTMLParser()
tree = etree.fromstring(html_data, parser)

# Find the footer element
footer = tree.xpath('//footer')[0]

# Find all the footer links and their XPaths
footer_links = footer.xpath('.//a')
link_xpaths = [tree.getpath(link) for link in footer_links]

# Save the scraped data as a CSV file
csv_file = 'scraped_data.csv'
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Link', 'XPath'])  # Write header
    writer.writerows(zip([link.text.strip() for link in footer_links], link_xpaths))

print(f"Scraped data saved to {csv_file}")