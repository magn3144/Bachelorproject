import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/ziprecruiter.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Initialize the list to store the scraped data
data = []

# Extract job descriptions
job_descriptions = tree.xpath('//div[@class="jobList-description"]/text()')
data.extend(job_descriptions)

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Job Description'])
    writer.writerows([[job_description] for job_description in data])