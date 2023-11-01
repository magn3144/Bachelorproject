import csv
from lxml import etree

# Read the HTML file
html_path = 'downloaded_pages/employmentfirstfl.html'
with open(html_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
html_tree = etree.HTML(html_content)

# Find all paragraphs in the main article
paragraphs = html_tree.xpath('/html/body/div/div/div/main/article/div/p')

# Extract the text from paragraphs
text_list = [paragraph.text.strip() for paragraph in paragraphs]

# Save the scraped data as a CSV file
csv_path = 'scraped_data.csv'
with open(csv_path, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    for text in text_list:
        writer.writerow([text])