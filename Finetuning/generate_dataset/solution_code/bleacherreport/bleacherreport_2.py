import csv
from lxml import html
  
# Read the local HTML file
with open('downloaded_pages/bleacherreport.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Extract the titles of the articles
titles = tree.xpath('//h3/text()')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    for title in titles:
        writer.writerow([title])