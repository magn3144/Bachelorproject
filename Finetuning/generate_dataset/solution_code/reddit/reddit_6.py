import csv
from lxml import html

def scrape_headers():
    # Load HTML file
    with open('downloaded_pages/reddit.html', 'r') as f:
        html_content = f.read()

    # Parse HTML
    tree = html.fromstring(html_content)

    # Find all header elements
    headers = tree.xpath('//h1 | //h2 | //h3 | //h4 | //h5 | //h6')

    # Extract header text
    header_text = [header.text_content() for header in headers]

    # Save header text to CSV file
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Header Text'])
        writer.writerows([[text] for text in header_text])

scrape_headers()