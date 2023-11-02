import csv
from lxml import etree

# Load the HTML file
with open('downloaded_pages/stackexchange-hot-questions.html', 'r') as f:
    html = f.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Find all the post tags
post_tags = tree.xpath('//a[@class="post-tag"]/text()')

# Find all the numbers of answers
answer_numbers = tree.xpath('//div[contains(@class, "stats")]/text()')

# Create a list of dictionaries containing the scraped data
data = []
for tag, number in zip(post_tags, answer_numbers):
    data.append({'Post Tag': tag, 'Number of Answers': number})

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Post Tag', 'Number of Answers']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)