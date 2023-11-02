import csv
from lxml import etree


def extract_text(xpath, element):
    elements = element.xpath(xpath)
    if elements:
        return elements[0].text.strip()
    return ''


def main():
    page_category = 'Government and Public Databases'
    page_elements = [
        {'xpath': '/html/body/div[3]/div/div/div[6]/div/h1', 'name': 'Census Datasets'},
    ]
    local_path = 'downloaded_pages/census.html'

    # Parse the HTML file
    with open(local_path, 'r') as f:
        html_content = f.read()
        tree = etree.HTML(html_content)

    # Extract the data
    data = {}
    for element in page_elements:
        xpath = element['xpath']
        name = element['name']
        text = extract_text(xpath, tree)
        data[name] = text

    # Save the data as CSV
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Category', 'Title'])
        writer.writerow([page_category, data['Census Datasets']])


if __name__ == '__main__':
    main()