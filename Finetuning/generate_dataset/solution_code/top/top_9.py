import csv
from lxml import etree

# Define the HTML file path
html_file = 'downloaded_pages/top.html'

# Define the XPaths
xpaths = {
    'link': '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/section/div/div/p/a',
}

# Parse the HTML file
with open(html_file, 'r') as f:
    html = f.read()
    tree = etree.HTML(html)

# Extract the scraped data
link_text = tree.xpath(xpaths['link'])[0].text

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Link Text'])
    writer.writerow([link_text])