import csv
from lxml import etree


def scrape_training_courses(html_file):
    courses = []
    with open(html_file, "r") as file:
        content = file.read()
    tree = etree.HTML(content)
    course_elements = tree.xpath("//h6[contains(@class, 'text-uppercase')]")

    for element in course_elements:
        courses.append(element.text)

    with open("scraped_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Training Courses"])
        for course in courses:
            writer.writerow([course])


scrape_training_courses("downloaded_pages/techasoft.html")