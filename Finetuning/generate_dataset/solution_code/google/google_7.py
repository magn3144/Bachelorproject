import csv
from lxml import etree

# Load the HTML file
with open('downloaded_pages/google.html', 'r') as f:
    html_content = f.read()

# Parse the HTML content
tree = etree.HTML(html_content)

# Get the title of the Doodle from the "This day in history" section
doodle_title_xpath = '/html/body/div[2]/div/ul/li[4]/div/h3'
doodle_title_element = tree.xpath(doodle_title_xpath)[0]
doodle_title = doodle_title_element.text.strip()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Doodle Title'])
    writer.writerow([doodle_title])