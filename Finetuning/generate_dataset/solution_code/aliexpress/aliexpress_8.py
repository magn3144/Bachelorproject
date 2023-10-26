import csv
from lxml import etree

# Define the HTML file path
html_file_path = 'downloaded_pages/aliexpress.html'

# Define the XPaths for the target elements
title_xpath = '/html/body/div[6]/div[1]/div/div[2]/div/div[2]/div[3]/a[18]/div[2]/div[3]/h1'

# Parse the HTML file
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()
    tree = etree.HTML(html_content)

# Extract the title
title_element = tree.xpath(title_xpath)[0]
title = title_element.text

# Save the scraped data as a CSV file
csv_file_path = 'scraped_data.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    writer.writerow([title])