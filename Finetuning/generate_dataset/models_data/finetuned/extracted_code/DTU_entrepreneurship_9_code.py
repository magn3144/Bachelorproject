
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as f:
    content = f.read()

# Parse the HTML
tree = html.fromstring(content)

# Find the department name and link
department_name = tree.xpath('//*[@id="footerDepartments"]/h2')[0].text
department_link = tree.xpath('//*[@id="footerDepartments"]/ul/li[1]/a')[0].attrib['href']

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([department_name, department_link])
