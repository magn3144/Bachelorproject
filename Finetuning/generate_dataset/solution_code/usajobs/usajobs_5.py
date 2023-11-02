import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/usajobs.html', 'r', encoding='utf-8') as file:
    page_content = file.read()

# Parse the HTML content
tree = html.fromstring(page_content)

# Find the job categories from the search filters
job_categories = tree.xpath('//div[@class="usajobs-search-filters__label"]/text()')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Job Category'])
    writer.writerows(zip(job_categories))