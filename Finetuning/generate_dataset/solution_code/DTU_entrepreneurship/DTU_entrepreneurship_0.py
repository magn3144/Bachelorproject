import csv
import re
from lxml import html

with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as file:
    page = file.read()

tree = html.fromstring(page)

course_elements = tree.xpath('//*[contains(text(),"ECTS")] | //*[contains(text(),"ects")]')

course_list = []
for element in course_elements:
    course_info = element.text.strip()
    match = re.search(r'^(.*\|) *(.*) (ECTS|ects).*$', course_info)
    if match:
        course_name = match.group(1).strip(' |')
        course_ects = match.group(2).strip()
        course_list.append((course_name, course_ects))

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Course Name", "ECTS"])
    writer.writerows(course_list)