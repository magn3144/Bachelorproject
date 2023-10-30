import csv
from bs4 import BeautifulSoup

# Load the HTML file
file_path = 'downloaded_pages/wordpress.html'
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find the heading text from the "Related sites" section
related_sites_heading = soup.find('h3', class_='wp-block-heading', text='Related sites')
related_sites_text = related_sites_heading.text if related_sites_heading else ''

# Save the scraped data as a CSV file
data = {'Category': 'Blogs', 'Heading': related_sites_text}
csv_file_path = 'scraped_data.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Category', 'Heading'])
    writer.writeheader()
    writer.writerow(data)