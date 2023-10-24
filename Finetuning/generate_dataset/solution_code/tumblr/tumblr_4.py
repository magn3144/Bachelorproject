import csv
import os
from lxml import etree

# File path
file_path = 'downloaded_pages/tumblr.html'

# XPaths
xpaths = {
    'blog_title': '/html/head/title',
    'post_contents': '//div[@class="rZlUD W45iW"]',
}

# Parse the HTML file
with open(file_path, 'r') as f:
    html = f.read()
tree = etree.HTML(html)

# Scrape the post contents
blog_titles = tree.xpath(xpaths['blog_title'])
post_contents = tree.xpath(xpaths['post_contents'])

# Remove duplicates and pairing blog titles with post contents
data = list(set(zip(blog_titles, post_contents)))

# Save data to a CSV file
output_path = 'scraped_data.csv'
if os.path.exists(output_path):
    os.remove(output_path)
with open(output_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Blog Title', 'Post Content'])
    writer.writerows(data)