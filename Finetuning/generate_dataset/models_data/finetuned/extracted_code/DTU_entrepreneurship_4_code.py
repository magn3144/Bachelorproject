
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find all courses on the page
courses = tree.xpath('//div[contains(@class, "course")]')

# Create a list to store the scraped data
scraped_data = []

# Iterate over the courses
for course in courses:
    # Get the course name and semester
    course_name = course.xpath('.//h2/span/text()')[0].strip()
    semester = course.xpath('.//h2/span[2]/text()')[0].strip()

    # Save the data
    scraped_data.append([semester, course_name])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Semester', 'Course Name'])
    writer.writerows(scraped_data)
