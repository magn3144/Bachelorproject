import csv
from lxml import etree

# Open the HTML file
html_file = open('downloaded_pages/google news.html', 'r', encoding='utf-8')
html_data = html_file.read()

# Parse the HTML
tree = etree.HTML(html_data)

# Find all the <a> tags with class "brSCsc"
elements = tree.xpath('//a[@class="brSCsc"]')

# Extract the text and corresponding XPaths
data = []
for elem in elements:
    text = elem.text.strip()
    xpath = tree.getpath(elem)
    data.append((text, xpath))

# Save the data as a CSV file
with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Text', 'XPath'])
    writer.writerows(data)