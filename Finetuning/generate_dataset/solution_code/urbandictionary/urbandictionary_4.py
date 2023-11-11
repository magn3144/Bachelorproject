import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/urbandictionary.html', 'r') as f:
    html_content = f.read()

# Parse the HTML content
html_tree = etree.HTML(html_content)

# Find the "Define a Word" link
link_element = html_tree.xpath('//a[@class="nav-link" and text()="Define a Word"]')[0]

# Extract the link's attributes
link_text = link_element.text
link_xpath = html_tree.getpath(link_element)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Link Text', 'XPath'])
    writer.writerow([link_text, link_xpath])