import csv
import requests
from lxml import etree

# Define the page URL
url = 'https://www.bloomberg.com'

# Load the HTML file
html = etree.parse('downloaded_pages/bloomberg.html', etree.HTMLParser())

# Find the headlines using their XPaths
headlines = html.xpath('''/html/body/div[1]/div[2]/div[2]/div[2]//h3[contains(@class, 'styles_itemHeadline__MNgSa')]
                        | /html/body/div[1]/div[2]/div[2]/div[2]//h3[contains(@class, 'article-story__eyebrow')]
                        | /html/body/div[1]/div[2]/div[2]/div[2]//p[contains(@class, 'article-story__headline')]''')

# Extract the text from the headlines
headlines_text = [headline.text.strip() for headline in headlines]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline'])
    writer.writerows([[headline] for headline in headlines_text])