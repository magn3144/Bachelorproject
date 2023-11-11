import csv
from lxml import etree

# Define the target HTML file path
html_file_path = "downloaded_pages/DTU-entrepreneurship.html"

# Define the XPaths for the desired elements
course_heading_xpath = "/html/body/form/div[3]/div[5]/h1"

# Parse the HTML file
tree = etree.parse(html_file_path)

# Retrieve the text from the "All entrepreneurship courses" heading
course_heading_element = tree.xpath(course_heading_xpath)[0]
course_heading_text = course_heading_element.text.strip()

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Category", "Task", "Scraped Data"])
    writer.writerow(["Educational Websites", "Retrieve the text from 'All entrepreneurship courses' heading", course_heading_text])