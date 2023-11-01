import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/ældresagen.html', 'r', encoding='utf-8') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Extract the text of the menu button using XPath
menu_button_text = tree.xpath('/html/body/div[2]/header/div[4]/div[2]/div[1]/button/span/text()')[0]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Menu Button Text'])
    writer.writerow([menu_button_text])