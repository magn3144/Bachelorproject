import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/avsforum.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Scrape all the thread titles
titles = tree.xpath('//h1[@class="MessageCard__thread-title"]/text()')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Thread Title'])
    writer.writerows(zip(titles))