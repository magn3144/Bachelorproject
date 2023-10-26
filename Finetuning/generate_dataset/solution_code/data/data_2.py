import csv
from lxml import etree


def extract_search_label(filename):
    # Load HTML file
    with open(filename, 'r') as file:
        html = file.read()

    # Parse HTML
    parser = etree.HTMLParser()
    tree = etree.fromstring(html, parser)

    # Extract search label element
    search_label_xpath = '/html/body/div[2]/div/div[6]/div/div[1]/div/form/label'
    search_label_element = tree.xpath(search_label_xpath)[0]

    # Clean and extract text
    search_label_text = search_label_element.text.strip()

    # Save extracted data as CSV
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Search Label'])
        writer.writerow([search_label_text])


# Run the function with the provided HTML file path
extract_search_label('downloaded_pages/data.cdc.html')