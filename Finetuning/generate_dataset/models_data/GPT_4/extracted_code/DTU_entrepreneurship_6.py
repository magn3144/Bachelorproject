import csv
import requests
from lxml import html

def scrape_course_description(path):
    with open(path, "r") as file:
        page_contents = file.read()
    
    tree = html.fromstring(page_contents)
    
    course_descriptions = tree.xpath('//div[@class="course-description"]/p/text()')
    
    with open('scraped_data.csv', 'w') as f:
        writer = csv.writer(f)
        for desc in course_descriptions:
            writer.writerow([desc])
  
scrape_course_description("downloaded_pages/DTU_entrepreneurship.html")