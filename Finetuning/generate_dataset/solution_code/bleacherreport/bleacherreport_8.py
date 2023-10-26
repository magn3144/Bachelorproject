import csv
from lxml import html

# Open the HTML file and parse it
with open('downloaded_pages/bleacherreport.html', 'r') as f:
    page_content = f.read()
tree = html.fromstring(page_content)

# Find all the article descriptions
descriptions = tree.xpath('//p[@class="atom articleDescription"]/text()')

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Description'])
    writer.writerows(descriptions)