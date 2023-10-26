import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/careerbuilder.html', 'r') as file:
    html_data = file.read()

# Parse the HTML
html_tree = etree.HTML(html_data)

# Scrape all the job salaries
job_salaries = html_tree.xpath('//h3[contains(@class, "pb")]//text()')

# Compile the scraped data into a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Salary'])
    for salary in job_salaries:
        writer.writerow([salary])