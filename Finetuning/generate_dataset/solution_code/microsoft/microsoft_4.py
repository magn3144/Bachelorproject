import csv
from lxml import etree

# Define the XPaths for the category and article titles
category_xpath = '/html/body/div/div[2]/div/div/header/div/div/div[4]/div[1]/nav/ul/li/div/ul/li[3]/span'
article_xpath = '/html/body/div/div[2]/div/div/header/div/div/nav/ul/li[6]/div/ul/li[2]/a'

# Load the HTML file
html_file = 'downloaded_pages/microsoft.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Create an HTML tree from the content
tree = etree.HTML(html_content)

# Get the category name
category_element = tree.xpath(category_xpath)[0]
category = category_element.text.strip()

# Get the article titles
article_elements = tree.xpath(article_xpath)
article_titles = [element.text.strip() for element in article_elements]

# Save the scraped data as a CSV file
csv_file = 'scraped_data.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Category', 'Article Title'])
    writer.writerow([category, ''])
    for title in article_titles:
        writer.writerow(['', title])