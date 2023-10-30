import csv
from lxml import etree

# Define the HTML file path
html_file_path = 'downloaded_pages/globestudios.html'

# Define the XPaths of the target elements
xpaths = [
    '/html/body/div/div[3]/div[6]/div/div/div[1]/div/h2[@class="h3"]',  # Bliv en del af Globe Club
]

# Read the HTML file
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create an ElementTree object from the HTML content
tree = etree.HTML(html_content)

# Scrape the text from the target elements using XPaths
scraped_data = []
for xpath in xpaths:
    elements = tree.xpath(xpath)
    if elements:
        text = elements[0].text.strip() if elements[0].text else ''
        scraped_data.append(text)

# Save the scraped data as a CSV file
csv_file_path = 'scraped_data.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Bliv en del af Globe Club'])  # Write the header
    for data in scraped_data:
        writer.writerow([data])  # Write each row