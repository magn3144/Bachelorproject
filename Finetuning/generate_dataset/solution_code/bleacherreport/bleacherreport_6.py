import csv
from lxml import html

# Define the target HTML file path
html_file = 'downloaded_pages/bleacherreport.html'

# Read the HTML file and create an HTML tree
with open(html_file, 'r') as file:
    html_content = file.read()
tree = html.fromstring(html_content)

# Scrape the text within the <a> tags
a_elements = tree.xpath('//a')
a_text = [a.text_content() for a in a_elements]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Text'])
    writer.writerows([[text] for text in a_text])