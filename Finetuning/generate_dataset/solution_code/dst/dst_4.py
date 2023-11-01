import csv
from lxml import etree

# Load the HTML file
with open('downloaded_pages/dst.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Create an lxml element tree
tree = etree.HTML(html)

# Find the documentation element
documentation_element = tree.xpath('/html/body/div[1]/main/div/div[2]/div[1]/div/div/div[4]/div/div/div[2]/a')

# Get the text from the documentation element
documentation_text = documentation_element[0].text.strip() if documentation_element else ''

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Documentation'])
    writer.writerow([documentation_text])