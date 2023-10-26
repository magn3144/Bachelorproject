import csv
from lxml import etree

# Define the HTML file path and category
html_file_path = 'downloaded_pages/ziprecruiter.html'
category = 'Jobs'

# Define the XPath expressions for job posting dates
date_xpath = '/html/body/main/div/div/div/div/div[3]/div/ul/li/div[2]'

# Create an empty list to store the job posting dates
job_posting_dates = []

# Parse the HTML file
parser = etree.HTMLParser()
tree = etree.parse(html_file_path, parser)

# Find all job posting dates using the XPath expressions
dates = tree.xpath(date_xpath)

# Add the dates to the job_posting_dates list
for date in dates:
    job_posting_dates.append(date.text)

# Save the job posting dates to a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Category', 'Job Posting Date'])
    for date in job_posting_dates:
        writer.writerow([category, date])