import csv
from bs4 import BeautifulSoup


with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Get all h2 elements with class a-heading-h1 o-hero__title and div elements with class bannerPriorityHeader
# and store them in the same list in the order they appear in the HTML file
relevant_elements = soup.find_all(['h2', 'div'], class_=["a-heading-h1 o-hero__title", "bannerPriorityHeader"])

# Get the text of all elements in relevant_elements
course_names = {}
last_heading = None
for element in relevant_elements:
    # If its a h2 element
    if element.name == 'h2':
        course_names[element.text] = []
        last_heading = element.text
    # If its a div element
    elif element.name == 'div':
        course_names[last_heading].append(element.text)

# Remove commas and enter
for header, course_list in course_names.items():
    for i, course in enumerate(course_list):
        course_list[i] = course.replace(',', '').replace('\n', '')

# Remove empty elements
for header, course_list in course_names.items():
    course_list[:] = [course for course in course_list if course != '']

# Remove course names that are not courses (dont start with a number)
for header, course_list in course_names.items():
    course_list[:] = [course for course in course_list if course[0].isdigit()]

# Save the data to a CSV file
with open('scraped_data.csv', 'w') as file:
    writer = csv.writer(file)
    for header, course_list in course_names.items():
        for course in course_list:
            writer.writerow([header, course])