import csv
from lxml import html

# Define the target file path
file_path = "downloaded_pages/tripadvisor.html"

# Read the HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Scrape motel names near Esbjerg Lufthavn (EBJ)
motel_names = tree.xpath('//a[contains(@class, "cJTqz") and contains(text(), "Moteller i nærheden af Esbjerg Lufthavn (EBJ)")]')
motel_names = [motel.text for motel in motel_names]

# Save the scraped data as CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Motel Name'])
    writer.writerows(zip(motel_names))