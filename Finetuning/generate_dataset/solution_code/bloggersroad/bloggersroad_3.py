import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/bloggersroad.html', 'r') as f:
    html = f.read()

# Parse the HTML
tree = etree.HTML(html)

# Find all recent posts
recent_posts = tree.xpath('//h4[@class="widget-title"]/text()')

# Get the corresponding XPaths
xpaths = tree.xpath('//h4[@class="widget-title"]/following-sibling::ul/li/a/@href')

# Combine recent posts and XPaths as rows in a CSV file
rows = zip(recent_posts, xpaths)

# Write the data to a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Post', 'XPath'])
    writer.writerows(rows)
