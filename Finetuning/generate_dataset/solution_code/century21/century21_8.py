import csv
from lxml import etree

def extract_mortgage_resources(html_file):
    with open(html_file, 'r') as file:
        html_content = file.read()

    parser = etree.HTMLParser()
    tree = etree.fromstring(html_content, parser)

    mortgage_resources = []

    mortgage_resources_xpath = "//h4[contains(text(), 'Mortgage Resources')]/following-sibling::ul/li"
    mortgage_resources_elements = tree.xpath(mortgage_resources_xpath)

    for element in mortgage_resources_elements:
        mortgage_resources.append(element.text.strip())

    with open('scraped_data.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Mortgage Resource'])
        writer.writerows(zip(mortgage_resources))

# Run the function
extract_mortgage_resources('downloaded_pages/century21.html')