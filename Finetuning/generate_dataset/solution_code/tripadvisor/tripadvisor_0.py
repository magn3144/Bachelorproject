import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/tripadvisor.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Find all restaurant names and ratings
restaurant_names = tree.xpath('//h1[contains(text(), "Restauranter i Vejen")]/following-sibling::div[contains(@class, "osNWb")]/text()')
restaurant_ratings = tree.xpath('//h3[contains(text(), "Vurdering fra rejsende")]/following-sibling::div[contains(@class, "osNWb")]/div/span[@class="YECgr"]/text()')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Restaurant Name', 'Rating'])
    writer.writerows(zip(restaurant_names, restaurant_ratings))