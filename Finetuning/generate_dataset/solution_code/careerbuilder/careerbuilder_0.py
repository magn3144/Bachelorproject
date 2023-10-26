import csv
from lxml import etree

# Define the target HTML file path
html_file_path = 'downloaded_pages/careerbuilder.html'

# Define the XPaths for the job titles
job_title_xpaths = [
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[4]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[3]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[4]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[2]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[1]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[4]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[3]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[4]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[4]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[3]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[4]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[2]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[1]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[4]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[1]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[4]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[2]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[3]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[4]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[3]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[1]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[4]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[3]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[2]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[3]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[4]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[2]/div/div/div/ul/li/a',
    '/html/body/div[1]/div/div[2]/main/div/div[2]/div[2]/div[1]/div[1]/div/div/div/ul/li/a'
]

# Create a list to store the scraped job titles
job_titles = []

# Parse the HTML file
tree = etree.parse(html_file_path)

# Extract the job titles using XPaths
for xpath in job_title_xpaths:
    result = tree.xpath(xpath)
    for element in result:
        job_titles.append(element.text)

# Save the scraped job titles as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Job Title'])
    writer.writerows([[job_title] for job_title in job_titles])