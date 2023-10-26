import csv
from lxml import etree

def scrape_jobs():
    # Load the HTML file
    with open('downloaded_pages/dk.indeed.html', 'r', encoding='utf-8') as file:
        html = file.read()

    # Parse the HTML
    parser = etree.HTMLParser()
    tree = etree.fromstring(html, parser)

    # Find all job listings
    job_listings = tree.xpath("//ul[@class='jobsearch-Results']/li")

    # Initialize a list to store the job types
    job_types = []

    # Iterate over each job listing
    for job_listing in job_listings:
        # Find the job type element and extract the text
        job_type_element = job_listing.xpath(".//div[contains(@class, 'title')]//span[contains(@class, 'job-type-icon')]/following-sibling::span[1]")
        if job_type_element:
            job_type = job_type_element[0].text
        else:
            job_type = ''

        # Append the job type to the list
        job_types.append(job_type)

    # Write the job types to a CSV file
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Job Type'])
        writer.writerows(zip(job_types))