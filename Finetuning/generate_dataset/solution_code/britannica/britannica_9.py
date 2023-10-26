# Importing the necessary libraries
import csv
from lxml import etree

# Defining the XPath expressions for the featured categories
featured_categories_xpath = "/html/body/main/div/div/div/h2[5]/following-sibling::div[@class='rw-member-list-wrapper']/a/text()"

# Opening the HTML file
with open('downloaded_pages/britannica.html', 'r') as file:
    html = file.read()

# Parsing the HTML
tree = etree.HTML(html)

# Extracting the featured categories
featured_categories = tree.xpath(featured_categories_xpath)

# Writing the extracted data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Featured Categories'])
    writer.writerows(zip(featured_categories))