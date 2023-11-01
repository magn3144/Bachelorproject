import csv
import requests
from lxml import html

# Set up the web scraping task details
category = "Social Media"
task = "Scrape all job titles and company names from a job search website"
local_path = "downloaded_pages/twitch.html"

# Load the HTML file
with open(local_path, 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Define the XPaths for job titles and company names
job_title_xpath = "//h2[@class='job-title']//text()"
company_name_xpath = "//span[@class='company-name']//text()"

# Extract the job titles and company names using the defined XPaths
job_titles = tree.xpath(job_title_xpath)
company_names = tree.xpath(company_name_xpath)

# Combine the job titles and company names into a list of tuples
data = list(zip(job_titles, company_names))

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Job Title', 'Company Name'])
    writer.writerows(data)