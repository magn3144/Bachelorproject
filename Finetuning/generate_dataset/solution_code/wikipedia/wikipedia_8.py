import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/wikipedia.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Parse the HTML
root = etree.HTML(html)

# Find all project names
project_elements = root.xpath("//div[@class='vector-menu-heading' and contains(text(), 'Wikipedia's sister projects')]/following-sibling::ul[1]//a")
project_names = [element.text.strip() for element in project_elements]

# Save the data as CSV
with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Project Name'])
    writer.writerows([[name] for name in project_names])