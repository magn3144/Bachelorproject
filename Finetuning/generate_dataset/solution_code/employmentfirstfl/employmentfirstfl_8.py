import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/employmentfirstfl.html', 'r') as f:
    html_content = f.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Retrieve the text from the figcaption tag in the main article
figcaption_elements = tree.xpath('//main/article/div/figure/figcaption')
captions = [elem.text_content().strip() for elem in figcaption_elements]

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Caption'])
    writer.writerows([[caption] for caption in captions])