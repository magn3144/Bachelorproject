import csv
import re
from bs4 import BeautifulSoup

def extract_courses(file_path):
    with open(file_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')

    courses = []
    for span in soup.find_all('span'):
        if re.match(r'\d{5}', span.text):
            course = {}
            course['name'] = span.text
            next_sibling = span.find_next_sibling('h2')
            if next_sibling:
                course['semester'] = next_sibling.text
            courses.append(course)

    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'semester'])
        writer.writeheader()
        writer.writerows(courses)

extract_courses('downloaded_pages/DTU_entrepreneurship.html')