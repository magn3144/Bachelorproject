import csv
from lxml import html

# Open the HTML file and parse it
with open('downloaded_pages/nytimes.html') as file:
    page = html.parse(file)

# Find the parent element of the "Living" section
living_section = page.xpath('//h3[contains(text(), "Living")]/parent::div/ol')[0]

# Find all the article titles in the "Living" section
article_titles = living_section.xpath('.//h3[@class="css-1kv6qi e15t083i0"]/text()')

# Save the article titles as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    writer.writerows([[title] for title in article_titles]) 