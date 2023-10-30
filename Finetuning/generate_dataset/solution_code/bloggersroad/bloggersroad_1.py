import csv
from lxml import etree

# Define the HTML file path
html_file = 'downloaded_pages/bloggersroad.html'

# Define the category name and its XPath
category_name = 'Blogs'
category_xpath = "/html/body/div/header/div[2]/div/div/nav/ul/li[2]/a"

# Create a CSV file to save the scraped data
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the category name and its XPath to the CSV file
    writer.writerow(['Category Name', 'XPath'])
    writer.writerow([category_name, category_xpath])

# Parse the HTML file
tree = etree.parse(html_file)

# Find the element using the category XPath
category_element = tree.xpath(category_xpath)[0]

# Print the category name
print(f"Category Name: {category_element.text}")