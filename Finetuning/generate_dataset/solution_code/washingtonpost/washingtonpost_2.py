import csv
import lxml.html as lh

# Define the XPath expressions for category names and article titles
category_xpath = "//nav[@data-qa='{category}']//a[@data-pb-field='category-name']"
title_xpath = "//h3[contains(@class, 'font--headline')]"

# Read the HTML file
with open('downloaded_pages/washingtonpost.html', 'r') as file:
    content = file.read()

# Create a document tree from the HTML content
doc = lh.fromstring(content)

# Find all category names
categories = doc.xpath(category_xpath.format(category='category'))

# Find all article titles
titles = doc.xpath(title_xpath)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Title'])
    for category, title in zip(categories, titles):
        writer.writerow([category.text_content(), title.text_content()])