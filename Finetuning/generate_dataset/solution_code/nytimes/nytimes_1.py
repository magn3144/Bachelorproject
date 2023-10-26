import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/nytimes.html', 'r') as f:
    html = f.read()

# Parse the HTML
root = etree.HTML(html)

# Find the headlines using the given XPath
headlines = root.xpath('/html/body/div/div[2]/main/section/div[1]/section[1]/div[1]/ol/li/div/article/a/h3/text()')

# Save the headlines as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Headline'])
    writer.writerows(zip(headlines))