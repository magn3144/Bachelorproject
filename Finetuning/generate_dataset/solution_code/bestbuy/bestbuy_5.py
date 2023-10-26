import csv
from lxml import html

# Define the target HTML file path
html_file_path = 'downloaded_pages/bestbuy.html'

# Define the XPaths for the relevant elements
title_xpath = '/html/head/title'
reviews_xpath = '//span[contains(@class, "c-reviews")]'

# Define the XPaths for the playstation product reviews
product_reviews_xpath = '//span[contains(text(), "PlayStation")]/ancestor::li//span[contains(@class, "c-reviews")]'

# Parse the HTML file
with open(html_file_path, 'r') as file:
    html_content = file.read()
    tree = html.fromstring(html_content)

# Scrape the title
title_element = tree.xpath(title_xpath)[0]
title = title_element.text.strip()

# Scrape the reviews
reviews_elements = tree.xpath(reviews_xpath)
reviews = [element.text.strip() for element in reviews_elements]

# Scrape the product reviews
product_reviews_elements = tree.xpath(product_reviews_xpath)
product_reviews = [element.text.strip() for element in product_reviews_elements]

# Combine all the scraped data into a list of dictionaries
scraped_data = []
for review in product_reviews:
    scraped_data.append({'Review': review})

# Save the scraped data as a CSV file
csv_file_path = 'scraped_data.csv'
fieldnames = ['Review']

with open(csv_file_path, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(scraped_data)