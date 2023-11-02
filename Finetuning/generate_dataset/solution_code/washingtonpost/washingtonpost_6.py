import csv
import re
from lxml import html

# Open the HTML file and parse it as HTML
with open('downloaded_pages/washingtonpost.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

tree = html.fromstring(html_content)

# Scrape the date and article summaries
dates = tree.xpath('//span[contains(@class, "font-xxxs")]/text()')
article_summaries = tree.xpath('//div[contains(@class, "font-size-blurb")]/text()')

# Clean up the scraped data
dates = [re.sub(r'\s+', ' ', date.strip()) for date in dates]
article_summaries = [re.sub(r'\s+', ' ', summary.strip()) for summary in article_summaries]

# Combine the scraped data into a list of rows
data = list(zip(dates, article_summaries))

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Date', 'Article Summary'])
    writer.writerows(data)