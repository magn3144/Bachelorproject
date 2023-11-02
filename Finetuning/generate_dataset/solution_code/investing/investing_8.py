import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/investing.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Find all the bond names
bond_elements = tree.xpath("//a[contains(@class, 'inv-link') and contains(@class, 'navbar_multi_list_link__B8IEy') and contains(@class, 'text-xs') and contains(@class, 'desktop:font-bold')]")
bond_names = [element.text for element in bond_elements]

# Write the bond names to CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Bond Name'])
    writer.writerows(zip(bond_names))