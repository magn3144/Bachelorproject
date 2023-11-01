import csv
from lxml import etree

# Define the xpath for the job listings
job_name_xpath = "//a[contains(text(), 'Overseas Education Counselor Jobs')]/following-sibling::ul/li/a"
job_link_xpath = "//a[contains(text(), 'Overseas Education Counselor Jobs')]/following-sibling::ul/li/a/@href"

# Parse the HTML file
tree = etree.parse("downloaded_pages/techasoft.html")

# Get the job names and links
job_names = tree.xpath(job_name_xpath)
job_links = tree.xpath(job_link_xpath)

# Combine the job names and links into a list of tuples
job_data = [(name.text, link) for name, link in zip(job_names, job_links)]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Job Name", "Link"])
    writer.writerows(job_data)