import csv
from bs4 import BeautifulSoup

# Load the HTML file
with open("downloaded_pages/DTU-entrepreneurship.html", "r", encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "lxml")

xpath_departments_header1 = "/html/body/form/div[3]/footer/div[2]/div[1]/div/div[2]/nav/div[1]/div/div/div[3]/h2"
xpath_departments_header2 = "/html/body/form/div[3]/header/div[1]/div[2]/div/div[2]/nav/div[1]/div/div/div[3]/h2"

# Gather all department and centre names
departments = set()
for header in [xpath_departments_header1, xpath_departments_header2]:
    department_header = soup.select(header)
    if department_header:
        department_links = department_header[0].find_next_sibling('ul').find_all('a')
        for link in department_links:
            departments.add(link.text.strip())

# Save results in a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Department / Center"])
    for department in departments:
        writer.writerow([department])