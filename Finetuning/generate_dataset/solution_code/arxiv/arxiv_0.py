import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/arxiv.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Scrape primary subjects using XPath
subjects = tree.xpath('//span[@class="primary-subject"]/text()')

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Primary Subjects'])
    writer.writerows([[subject] for subject in subjects])