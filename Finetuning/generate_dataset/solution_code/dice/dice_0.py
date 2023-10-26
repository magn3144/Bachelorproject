import csv
from lxml import html

def extract_job_titles(html_file):
    with open(html_file, 'rb') as f:
        tree = html.fromstring(f.read())
    
    job_titles = tree.xpath("//a[contains(@class, 'card-title-link')]/text()")
    
    return job_titles

def save_to_csv(data, csv_file):
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Job Title'])
        for item in data:
            writer.writerow([item])

html_file = 'downloaded_pages/dice.html'
csv_file = 'scraped_data.csv'

job_titles = extract_job_titles(html_file)
save_to_csv(job_titles, csv_file)