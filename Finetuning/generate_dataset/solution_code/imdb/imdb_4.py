import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/imdb.html', 'r') as file:
    html_content = file.read()

# Create an XPath parser
parser = etree.HTMLParser()
tree = etree.fromstring(html_content, parser)

# Extract the titles and positions
titles = tree.xpath('//h3[@class="ipc-title__text"]/text()')
positions = tree.xpath('//ul[@class="ipc-chart-title-list ipc-chart-title-list--base"]/li/div[2]/div/div/div[1]/a/h3/text()')

# Combine titles and positions into a list of tuples
movies = [(position, title) for position, title in zip(positions, titles)]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Position', 'Title'])
    writer.writerows(movies)