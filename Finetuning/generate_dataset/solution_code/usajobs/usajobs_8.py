import csv
from lxml import html

# Define the HTML file path
file_path = "downloaded_pages/usajobs.html"

# Define the XPaths for the grade labels
grade_xpaths = [
    "/html/body/section/section/div/aside/div/div[2]/div[3]/div[1]/ul/li[2]/div/div[2]/ul/li[3]/label",
    "/html/body/section/section/div/aside/div/div[2]/div[3]/div[1]/ul/li[4]/div/div[2]/div[2]/div[5]/ul/li[10]/label",
    "/html/body/section/section/div/aside/div/div[2]/div[3]/div[1]/ul/li[3]/div/div[2]/section[2]/div[2]/h4[16]",
    "/html/body/section/section/div/aside/div/div[2]/div[3]/div[1]/ul/li[3]/div/div[2]/h5"
]

# Extract the grade labels
grades = []
with open(file_path, "r", encoding="utf-8") as html_file:
    page_content = html_file.read()
    tree = html.fromstring(page_content)
    for xpath in grade_xpaths:
        elements = tree.xpath(xpath)
        for element in elements:
            grades.append(element.text.strip())

# Save the grade labels as a CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    for grade in grades:
        writer.writerow([grade])