import csv
import lxml.html as lh

# Load the HTML file
path = 'downloaded_pages/dice.html'
with open(path, 'r', encoding='UTF-8') as f:
    html_content = f.read()

# Parse the HTML content
doc = lh.fromstring(html_content)

# Scrape job categories
job_categories = doc.xpath('//h2[contains(@id, "employer-nav-label")]')
job_categories = [category.text_content().strip() for category in job_categories]

# Save the scraped data as CSV
output_file = 'scraped_data.csv'
with open(output_file, 'w', newline='', encoding='UTF-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Job Category'])
    writer.writerows([[category] for category in job_categories])