import csv
from lxml import etree

# Load the HTML file
file_path = 'downloaded_pages/fbi.html'
with open(file_path, 'r') as f:
    html_content = f.read()

# Parse the HTML
html_tree = etree.HTML(html_content)

# Find all the links and names in the Terrorism category
terrorism_links = html_tree.xpath("//a[contains(text(), 'Terrorism')]")
terrorism_data = [(link.text, link.get('href')) for link in terrorism_links]

# Save the scraped data as CSV
output_file = 'scraped_data.csv'
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Link'])
    writer.writerows(terrorism_data)