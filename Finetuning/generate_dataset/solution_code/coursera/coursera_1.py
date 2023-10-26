import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/coursera.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find the menu items from the Subjects section
menu_items = tree.xpath('/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[1]/div/div/div[2]/ul/li[2]/button/span[2]')

# Write the menu items to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Menu Items'])
    for item in menu_items:
        writer.writerow([item.text])