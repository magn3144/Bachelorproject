import csv
import requests
from lxml import html

file_path = 'downloaded_pages/DTU_entrepreneurship.html'

with open(file_path, 'r') as file:
    page_content = file.read()

tree = html.fromstring(page_content)

course_titles = tree.xpath('//div[contains(@class,"view-course")]//h2/span/text()')
course_descriptions = tree.xpath('//div[contains(@class,"view-course")]//p/text()')

data = list(zip(course_titles, course_descriptions))

with open('scraped_data.csv', mode ='w', newline='') as file:
   
    writer = csv.writer(file)
    writer.writerow(['Title', 'Description'])
    writer.writerows(data)