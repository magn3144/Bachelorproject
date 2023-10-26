import csv
from lxml import etree

# Constants
HTML_PATH = "downloaded_pages/bbc.html"
XPATH_ARTICLE_TITLE = "//span[contains(@class, 'gs-c-promo-heading__title gel-pica-bold') and contains(text(), 'minimum tax rate')]/text()"
CSV_FILE = "scraped_data.csv"

# Parse HTML
parser = etree.HTMLParser()
tree = etree.parse(HTML_PATH, parser)

# Extract article titles
article_titles = tree.xpath(XPATH_ARTICLE_TITLE)

# Save data as CSV
with open(CSV_FILE, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Article Title'])
    writer.writerows([[title] for title in article_titles])

print(f"Scraped data saved as {CSV_FILE}")