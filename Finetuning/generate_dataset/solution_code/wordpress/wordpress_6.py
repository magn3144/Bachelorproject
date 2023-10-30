import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/wordpress.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Create an XML tree from the HTML string
parser = etree.HTMLParser()
tree = etree.fromstring(html, parser)

# Find the paragraph element using XPath
paragraph = tree.xpath('/html/body/div/main/div[2]/div/div[1]/div/p[3]')[0]

# Extract the text from the paragraph element
paragraph_text = paragraph.text.strip()

# Prepare the data for CSV
data = [['Category', 'Task', 'Text'],
        ['Blogs', 'Extract the paragraph text after "Tonal\'s comprehensive website provides an overview"', paragraph_text]]

# Save the data as CSV
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)