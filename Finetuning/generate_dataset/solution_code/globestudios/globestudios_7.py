import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/globestudios.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
root = etree.HTML(html_content)

# Find the "Din kurv er tom" element
element = root.xpath('/html/body/div/div[5]/div/div[2]/div[1]/p')[0]

# Get the text from the element
text = element.text.strip()

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Task', 'Text'])
    writer.writerow(['Clothing Websites', 'Retrieve "Din kurv er tom"', text])