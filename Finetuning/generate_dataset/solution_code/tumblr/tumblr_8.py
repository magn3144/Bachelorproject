import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/tumblr.html', 'r') as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Find the 'Check out these blogs' section
blogs_section = tree.xpath('//h1[text()="Check out these blogs"]/following-sibling::ul[1]')

# Extract the blog names
blog_names = [blog.text.strip() for blog in blogs_section[0].xpath('.//a')]

# Save the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for blog_name in blog_names:
        writer.writerow([blog_name])