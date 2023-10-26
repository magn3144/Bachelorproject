import csv
from lxml import etree

# Load the HTML file
with open('downloaded_pages/dice.html', 'r') as file:
    html = file.read()

# Create an XML element tree from the HTML
tree = etree.HTML(html)

# Find all salary information using XPath
salary_elements = tree.xpath("//span[contains(@class, 'salaryText')]")
salaries = [elem.text for elem in salary_elements]

# Save the salaries as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Salary'])
    for salary in salaries:
        writer.writerow([salary])