import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/careerbuilder.html', 'r') as f:
    html_text = f.read()

# Create an XML element tree
tree = etree.HTML(html_text)

# Locate the list of trending job searches
trending_jobs = tree.xpath('/html/body/div[1]/div/div[2]/main/div/div[2]/div[1]/h2')
job_list = [job.text.strip() for job in trending_jobs]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Trending Jobs'])
    writer.writerows(zip(job_list))