import csv
from lxml import html

# Define the file path
file_path = 'downloaded_pages/h&m.html'

# Define the XPaths
xpaths = {
    'facebook-logo': '/html/body/div/section/footer/div[2]/ul/li[1]/a/button/span[1]/svg/title'
}

# Create an empty dictionary to store the scraped data
scraped_data = {}

# Parse the HTML file
tree = html.parse(file_path)

# Extract the data using XPaths
for element_id, xpath in xpaths.items():
    element = tree.xpath(xpath)
    if element:
        scraped_data[element_id] = element[0].text.strip()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Element ID', 'Text Content'])
    for element_id, text_content in scraped_data.items():
        writer.writerow([element_id, text_content])