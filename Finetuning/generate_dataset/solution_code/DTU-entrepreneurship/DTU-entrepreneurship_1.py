import csv
from lxml import html

# Open the HTML file
local_path = 'downloaded_pages/DTU-entrepreneurship.html'
with open(local_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find the DTU.dk link
dtu_link_element = tree.xpath("/html/body/form/div[3]/footer/div[2]/div[1]/div/div[1]/a/span")[0]

# Get the text from the DTU.dk link
dtu_link_text = dtu_link_element.text.strip()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'DTU.dk Text'])
    writer.writerow(['Educational Websites', dtu_link_text])