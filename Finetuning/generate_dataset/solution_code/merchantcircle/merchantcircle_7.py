import csv
from lxml import etree

# Define the target XPath for reviews
reviews_xpath = '/html/body/div[1]/div[4]/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/div[1]/article/div[2]/div[1]/div[1]'

# Load the HTML file
with open('downloaded_pages/merchantcircle.html', 'r') as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Extract the reviews using the XPath
reviews = tree.xpath(reviews_xpath)

# Prepare the scraped data
scraped_data = []
for review in reviews:
    scraped_data.append(review.text.strip())

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review'])
    writer.writerows(zip(scraped_data))