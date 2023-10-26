import csv
from lxml import etree

def scrape_related_searches(html_file):
    # Load the HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Parse the HTML
    tree = etree.HTML(html_content)

    # Find the related searches elements using XPaths
    related_searches_elements = tree.xpath('/html/body/div[3]/div[2]/div[1]/div/dl/dt')

    # Extract the text from the related searches elements
    related_searches = [element.text.strip() for element in related_searches_elements]

    return related_searches

def save_to_csv(data, filename):
    # Write the data to a CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Related Searches'])
        writer.writerows([[search] for search in data])

# Define the local path to the HTML file
html_path = 'downloaded_pages/alibaba.html'

# Scrape the related searches
related_searches = scrape_related_searches(html_path)

# Save the data to a CSV file
save_to_csv(related_searches, 'scraped_data.csv')