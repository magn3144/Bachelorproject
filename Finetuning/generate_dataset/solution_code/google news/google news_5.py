import csv
from lxml import html

def scrape_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content

def extract_data(html_content):
    tree = html.fromstring(html_content)
    h1_elements = tree.xpath('//h1[contains(@class, "Da1Shd")]')
    data = []
    for element in h1_elements:
        text = element.text_content()
        xpath = tree.getpath(element)
        data.append({'text': text, 'xpath': xpath})
    return data

def save_data_as_csv(data):
    headers = ['text', 'xpath']
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

def main():
    file_path = 'downloaded_pages/google news.html'
    html_content = scrape_html_file(file_path)
    data = extract_data(html_content)
    save_data_as_csv(data)

if __name__ == '__main__':
    main()