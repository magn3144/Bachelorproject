import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/dk.indeed.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = etree.HTML(html_content)

# Find all job title elements
job_title_elements = tree.xpath("//span[@id='jobTitle-1bd8027dbe407ed4']")

# Extract the job titles
job_titles = [element.text for element in job_title_elements]

# Write the job titles to CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Job Title'])
    writer.writerows([[title] for title in job_titles])