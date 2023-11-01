import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/wikipedia.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Scrape the number of articles available
articles_element = tree.xpath('/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[3]/div/p/a[2]')[0]
articles = articles_element.text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Number of Articles'])
    writer.writerow(['Educational Websites', articles])