import csv
from lxml import etree

def extract_data_from_html(html):
    tree = etree.parse(html)
    job_locations = tree.xpath("//span[contains(@class, 'search-result-location')]/text()")

    return job_locations

def save_data_as_csv(data):
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Job Location'])
        writer.writerows(data)

def main():
    html_file = 'downloaded_pages/dice.html'
    job_locations = extract_data_from_html(html_file)
    save_data_as_csv(job_locations)

if __name__ == '__main__':
    main()