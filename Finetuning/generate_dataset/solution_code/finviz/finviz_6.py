import csv
from lxml import html

# Open the HTML file
with open('downloaded_pages/finviz.html', 'r') as file:
    content = file.read()

# Create an HTML tree from the content
tree = html.fromstring(content)

# Get all instances of market caps
market_caps = tree.xpath('//th[contains(.,"Market Cap")]/following-sibling::td/a/text()')

# Write the scraped data to CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Market Cap'])
    writer.writerows(zip(market_caps))