import re
import csv
from lxml import html

html_path = 'downloaded_pages/DTU_entrepreneurship.html'
with open(html_path, 'r') as f:
    page_content = f.read()

tree = html.fromstring(page_content)

course_elems = tree.xpath('//span[starts-with(text(), "38")]')

course_info_list = []
for course in course_elems:
    course_info = course.text.strip()
    course_data = re.match(r'(.*? \| .*? ECTS)', course_info)
    if course_data:
        course_info_list.append(course_data.group(1))

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Course Name"])
    for course_info in course_info_list:
        writer.writerow([course_info])