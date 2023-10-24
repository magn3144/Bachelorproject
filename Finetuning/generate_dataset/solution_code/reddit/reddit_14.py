import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/reddit.html', 'rb') as file:
    html_data = file.read()

# Parse the HTML
tree = html.fromstring(html_data)

# Define the XPaths of the comments
xpaths = [
    '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div/div/div/div/div/div',
    '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div/span/span',
    '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div/span/span/span/span',
]

# Find all the comments
comments = []
for xpath in xpaths:
    comments.extend(tree.xpath(xpath))

# Filter the golden comments
golden_comments = [comment.text_content() for comment in comments if 'gold' in comment.classes]

# Save the golden comments to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Comments'])
    writer.writerows([[comment] for comment in golden_comments])