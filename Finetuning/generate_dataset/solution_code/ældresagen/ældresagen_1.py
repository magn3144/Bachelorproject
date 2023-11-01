import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/ældresagen.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Scrape the name of the doctor in the header
doctor_name = tree.xpath('/html/body/div[2]/header/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[2]/ul[4]/li[2]/a/text()')[0]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Task', 'Doctor Name'])
    writer.writerow(['News', 'Scrape the name of the doctor in the header', doctor_name])