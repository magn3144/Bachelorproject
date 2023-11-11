import csv
from lxml import etree

# Define the XPath for extracting news article descriptions
news_description_xpath = '/html/body/div[2]/main/div/div[3]/section/div/div[2]/section/div[5]/section/div/div/div/div/div/div'

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse('downloaded_pages/imdb.html', parser)

# Extract the news article descriptions
news_descriptions = tree.xpath(news_description_xpath)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['News Article Description'])
    writer.writerows([[desc.text.strip()] for desc in news_descriptions])