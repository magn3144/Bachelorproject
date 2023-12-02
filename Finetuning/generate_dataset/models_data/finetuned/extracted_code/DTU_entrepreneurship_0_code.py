
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find all course names and corresponding ECTS points
course_names = tree.xpath('//span[contains(text(), "Course name")]/following-sibling::span/text()')
ects_points = tree.xpath('//span[contains(text(), "ECTS points")]/following-sibling::span/text()')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Course name', 'ECTS points'])
    for course_name, ects_point in zip(course_names, ects_points):
        writer.writerow([course_name, ects_point])
