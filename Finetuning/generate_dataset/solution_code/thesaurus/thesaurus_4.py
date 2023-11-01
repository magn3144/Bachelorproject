import csv
from lxml import etree

# Define the target HTML file path
html_file_path = 'downloaded_pages/thesaurus.html'

# Define the target XPaths for synonyms of the day
synonyms_xpath = '/html/body/div/div/main/div[1]/div[1]/div/div/a'

# Parse the HTML file
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()
    parser = etree.HTMLParser()
    tree = etree.fromstring(html_content, parser)

# Extract the synonyms of the day
synonyms = tree.xpath(synonyms_xpath)

# Save the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Synonyms of the Day'])
    for synonym in synonyms:
        writer.writerow([synonym.text])