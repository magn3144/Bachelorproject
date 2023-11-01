import csv
from urllib.request import urlopen
from lxml import etree

# Open the HTML file
with open('downloaded_pages/quora.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
html_tree = etree.HTML(html_content)

# Find all post titles and authors using XPaths
post_title_elements = html_tree.xpath("//div[@class='q-box qu-py--small-spacing']/div/div[@class='q-box qu-mt--tiny-qu-mb--tiny'][1]/a[@class='q-box qu-display--block']")
post_author_elements = html_tree.xpath("//div[@class='q-box qu-py--small-spacing']/div/div[@class='q-box qu-mt--tiny-qu-mb--tiny'][2]")

# Extract the titles and authors
titles = [title.text for title in post_title_elements]
authors = [author.text for author in post_author_elements]

# Prepare the data as a list of dictionaries
data = [{'Title': title, 'Author': author} for title, author in zip(titles, authors)]

# Save the data to a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Title', 'Author'])
    writer.writeheader()
    writer.writerows(data)