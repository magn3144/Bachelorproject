import csv
from lxml import etree

# Define the target elements and their XPaths
target_elements = {
    "Delft University of Technology": "/html/body/div[1]/div[1]/div/main/div/div[5]/div/div[3]/div[28]/a/div/div[2]/div/div[2]/span/span[1]/span"
}

# Load the HTML file
with open('downloaded_pages/edx.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Parse the HTML
tree = etree.HTML(html_content)

# Scrape the target data
scraped_data = []
for element, xpath in target_elements.items():
    data = tree.xpath(xpath)
    if data:
        scraped_data.append([element, data[0].text])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Element', 'Text'])
    writer.writerows(scraped_data)