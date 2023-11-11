import csv
from lxml import html

# Open the HTML file
with open('downloaded_pages/DTU-entrepreneurship.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find all course titles
course_titles = tree.xpath('//h2[contains(@class, "a-heading-h1")]/text()')

# Save the course titles as a CSV file
with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Course Title'])
    writer.writerows([[title] for title in course_titles])