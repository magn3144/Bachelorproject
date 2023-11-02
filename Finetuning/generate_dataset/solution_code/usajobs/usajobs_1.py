import csv
from lxml import etree

# Load the HTML file
html_path = 'downloaded_pages/usajobs.html'
with open(html_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create an HTML tree from the content
tree = etree.HTML(html_content)

# Scrape the job titles and hiring paths
job_titles = tree.xpath('//h4[@class="usajobs-search-result--core__agency"]/text()')
hiring_paths = tree.xpath('//p[@class="usajobs-search-result--core__hiring-path"]/text()')

# Save the scraped data as CSV
csv_path = 'scraped_data.csv'
with open(csv_path, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Job Title', 'Hiring Path'])
    writer.writerows(zip(job_titles, hiring_paths))