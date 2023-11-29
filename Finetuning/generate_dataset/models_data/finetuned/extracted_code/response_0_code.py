import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find all course titles
course_titles = tree.xpath('//span[contains(@class, "course__title")]')

# Save the course titles as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Course Title'])
    for course_title in course_titles:
        writer.writerow([course_title.text])
