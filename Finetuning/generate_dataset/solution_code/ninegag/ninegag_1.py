import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/9gag.html', 'r') as file:
    html_content = file.read()

# Create an lxml tree from the HTML content
tree = html.fromstring(html_content)

# Extract all comments from the specific post
comments = tree.xpath('//div[@class="post-comments"]/ul[@class="comments"]/li[@class="comment"]/div[@class="comment-text"]/text()')

# Write the comments to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for comment in comments:
        writer.writerow([comment])