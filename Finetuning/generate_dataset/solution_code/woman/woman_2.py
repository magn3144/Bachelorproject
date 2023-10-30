import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/woman.html', 'r') as file:
    html_string = file.read()

# Parse the HTML string
html_tree = etree.HTML(html_string)

# Find the blog posts
blog_posts = html_tree.xpath("//h3[contains(text(), 'Fra redaktionen')]/following-sibling::div[@class='content-label-widget']")

# Scrape author names and publication dates
data = []
for post in blog_posts:
    author = post.xpath(".//a[@class='text-bold']/text()")[0].strip()
    date = post.xpath(".//div[@class='datetime']/text()")[0].strip()
    data.append([author, date])

# Save scraped data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Author', 'Publication Date'])
    writer.writerows(data)