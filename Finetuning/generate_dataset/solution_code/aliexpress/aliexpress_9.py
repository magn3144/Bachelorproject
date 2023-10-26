import csv
from lxml import etree

# Define the function to extract the text of the "Browse by Category" section
def extract_category_text(html):
    tree = etree.HTML(html)
    category_text = tree.xpath("/html/body/div[7]/div/div[2]/dl/dt")[0].text.strip()
    return category_text

# Read the HTML file
with open('downloaded_pages/aliexpress.html', 'r') as file:
    html = file.read()

# Extract the category text
category_text = extract_category_text(html)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category'])
    writer.writerow([category_text])