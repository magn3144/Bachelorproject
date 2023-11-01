import csv
from lxml import html


def get_insurance_companies(tree):
    insurance_companies = []
    spans = tree.xpath("//span[contains(text(),'Forsikringsselskab') or contains(text(),'forsikringsselskab')]")
    for span in spans:
        company_name = span.text
        insurance_companies.append(company_name)
    return insurance_companies


def scrape_page():
    with open('downloaded_pages/trustpilot.html', 'r', encoding='utf-8') as file:
        content = file.read()
    tree = html.fromstring(content)
    insurance_companies = get_insurance_companies(tree)
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Insurance Company Name'])
        writer.writerows(insurance_companies)


if __name__ == '__main__':
    scrape_page()