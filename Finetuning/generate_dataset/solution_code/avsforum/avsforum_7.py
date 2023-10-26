import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/avsforum.html', 'r') as f:
    html_string = f.read()

# Create an lxml HTML parser
parser = etree.HTMLParser()

# Parse the HTML string
tree = etree.fromstring(html_string, parser)

# Find all message cards
message_cards = tree.xpath('//div[contains(@class, "MessageCard")]')

# Scrape the post count from each message card
data = []
for card in message_cards:
    post_count = card.xpath('.//span[contains(@class, "MessageCard__post-count")]/text()')
    if len(post_count) > 0:
        data.append(post_count[0])

# Save the data as CSV
with open('scraped_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Post Count"])
    writer.writerows([[d] for d in data])