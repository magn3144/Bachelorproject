import csv
from lxml import html

# Open the local HTML file
with open('downloaded_pages/dk.indeed.html', 'r') as file:
    content = file.read()

# Parse the HTML content
tree = html.fromstring(content)

# Scrape job posting date information
job_dates = tree.xpath('//li[contains(@class, "result")]//span[contains(@class, "date")]//text()')

# Save the scraped data as CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Job Posting Date'])
    for job_date in job_dates:
        writer.writerow([job_date])