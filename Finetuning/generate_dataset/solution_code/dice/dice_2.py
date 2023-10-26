import csv
from lxml import etree

html_path = 'downloaded_pages/dice.html'
category = 'Jobs'

# Define XPaths for the HTML elements
xpaths = {
    'job_title': '/html/body/dhi-js-dice-client/div/dhi-search-page-container/dhi-search-page/div/dhi-search-page-results/div/div[3]/js-search-display/div/div[3]/dhi-search-cards-widget/div/*/div/div[1]/div/div[2]/div[1]/h5/a',
    'job_description': '/html/body/dhi-js-dice-client/div/dhi-search-page-container/dhi-search-page/div/dhi-search-page-results/div/div[3]/js-search-display/div/div[3]/dhi-search-cards-widget/div/*/div/div[2]/div[2]'
}

# Scrape the job data from the HTML file
with open(html_path, 'r') as file:
    html_content = file.read()

root = etree.HTML(html_content)
job_elems = root.xpath(xpaths['job_title'])
description_elems = root.xpath(xpaths['job_description'])

job_data = []

for job, description in zip(job_elems, description_elems):
    job_title = job.text.strip()
    job_description = description.text.strip()

    job_data.append({'Job Title': job_title, 'Job Description': job_description})

# Save the scraped data as a CSV file
csv_path = 'scraped_data.csv'

with open(csv_path, 'w', newline='', encoding='utf-8') as file:
    fieldnames = ['Job Title', 'Job Description']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(job_data)