import csv
from lxml import html

# Define the XPaths for extracting the paragraphs from the articles
paragraph_xpaths = [
    '/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article/div[2]/div[2]/div/p',
    '/html/body/div[1]/div/div[3]/div/main/div/ul/li/article/div[2]/div[2]/div/p',
    '/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article/div[2]/div[1]/div/p',
]

# Load the HTML file
with open('downloaded_pages/aljazeera.html', 'r') as file:
    page_content = file.read()

# Parse the HTML content
tree = html.fromstring(page_content)

# Extract the paragraphs from the articles using the defined XPaths
paragraphs = []
for xpath in paragraph_xpaths:
    elements = tree.xpath(xpath)
    paragraphs.extend(elements)

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows([[paragraph.text_content()] for paragraph in paragraphs])