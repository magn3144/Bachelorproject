import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/tripadvisor.html', 'r') as file:
    html = file.read()

# Create the XML tree from the HTML
tree = etree.HTML(html)

# Scrape the community section
community_posts = tree.xpath('//div[@class="bbs-content-row"]//div[@class="title"]/a')
data = []
for post in community_posts:
    title = post.text.strip()
    description = post.attrib['title'].strip()
    data.append([title, description])

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Description'])
    writer.writerows(data)