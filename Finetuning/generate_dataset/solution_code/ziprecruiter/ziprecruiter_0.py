import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/ziprecruiter.html', 'r') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find all job titles using XPath
job_titles = tree.xpath('//div[@class="jobList-description"]/text()')

# Write job titles to CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Job Title'])
    writer.writerows([[job_title] for job_title in job_titles])