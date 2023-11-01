import csv
from lxml import etree

# Load the HTML file
html_path = 'downloaded_pages/tripadvisor.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Parse the HTML
tree = etree.HTML(html)

# Find all hotels near Militarismen
hotel_elements = tree.xpath('//a[contains(text(), "Hoteller i nærheden af Militarismen")]')

# Extract the hotel names
hotel_names = [element.text for element in hotel_elements]

# Save the scraped data as a CSV file
csv_path = 'scraped_data.csv'
with open(csv_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Hotel Name'])
    for name in hotel_names:
        writer.writerow([name])