import csv
from lxml import etree


def parse_html(html_file):
    with open(html_file, 'r') as file:
        return etree.parse(file, parser=etree.HTMLParser())


def scrape_footer_details(tree):
    footer_elements_xpath = '/html/body/main/div/span[2]/div/div/footer/div/ul/li'
    footer_elements = tree.xpath(footer_elements_xpath)
    footer_details = []

    for element in footer_elements:
        footer_text = element.text.strip()
        footer_details.append(footer_text)

    return footer_details


def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Footer Details'])

        for item in data:
            writer.writerow([item])


if __name__ == '__main__':
    html_file = 'downloaded_pages/dk.indeed.html'
    tree = parse_html(html_file)
    footer_details = scrape_footer_details(tree)
    save_to_csv(footer_details)