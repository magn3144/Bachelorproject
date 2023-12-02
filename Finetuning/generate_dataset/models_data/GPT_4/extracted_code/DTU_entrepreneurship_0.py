import csv
import re
from lxml import etree
from lxml.html import parse

html_file = "downloaded_pages/DTU_entrepreneurship.html"
tree = parse(html_file)
root = tree.getroot()

course_elements = root.xpath("//div[contains(@class, 'module module-generic clearfix')]")
course_data = []
for course in course_elements:
    title = course.xpath(".//h2/span/text()")
    ects = re.search('\d+ ECTS', course.text_content())
    if title and ects:
        course_data.append([title[0], ects.group()])

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Course Title", "ECTS"])
    writer.writerows(course_data)