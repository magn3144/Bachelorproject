import csv
from lxml import etree

# Define the target HTML file path
html_path = "downloaded_pages/dk.indeed.html"

# Define the XPath expressions for the job descriptions
# Update the XPath expressions based on the provided HTML elements
xpaths = [
    '/html/body/main/div/div[1]/div/div[5]/div[1]/div[5]/div/ul/li/div/div[1]/div/div[1]/div/table[2]/tbody/tr[2]/td/div[1]/div',
    '/html/body/main/div/div[1]/div/div[5]/div[1]/div[5]/div/ul/li/div/div[1]/div/div[1]/div/table[2]/tbody/tr[2]/td/div[1]/div/ul/li',
    '/html/body/main/div/div[1]/div/div[5]/div[1]/div[5]/div/ul/li/div/div[1]/div/div[1]/div/table[2]/tbody/tr[2]/td/div[1]/div/ul/li[1]'
]

# Scrape the job descriptions
def scrape_job_descriptions():
    # Parse the HTML file
    with open(html_path, "r") as file:
        html_content = file.read()
    html_tree = etree.HTML(html_content)

    job_descriptions = []

    # Extract the job descriptions from the HTML using the XPath expressions
    for xpath in xpaths:
        elements = html_tree.xpath(xpath)
        for element in elements:
            job_descriptions.append(element.text.strip())

    # Return the scraped job descriptions
    return job_descriptions

# Save the scraped data as a CSV file
def save_scraped_data(job_descriptions):
    with open("scraped_data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Description"])
        writer.writerows([[job_description] for job_description in job_descriptions])

# Execute the scraping and saving functions
job_descriptions = scrape_job_descriptions()
save_scraped_data(job_descriptions)