import csv
from lxml import etree


def extract_element_text(html, xpath):
    try:
        element = html.xpath(xpath)[0]
        return element.text.strip()
    except IndexError:
        return ''


def scrape_data():
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Category', 'Search Term'])

        with open('downloaded_pages/reddit.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        html = etree.HTML(content)

        title = extract_element_text(html, '/html/head/title')
        writer.writerow(['Page Title', title])

        search_terms = [
            extract_element_text(html, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[47]/div/div/div/div[2]/div[2]/div[2]/div/p[1]/a[1]'),
            extract_element_text(html, '/html/body/div[1]/div/div[2]/div[3]/div/section/div/section[1]/div/span[3]/a[2]'),
            extract_element_text(html, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[205]/div/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/template/button/span[2]/span'),
            extract_element_text(html, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[4]/a'),
            extract_element_text(html, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[3]/div/div/div/div[2]/div[2]/div[1]/span/div/div/div/a')
        ]

        for term in search_terms:
            writer.writerow(['Social Media', term])


if __name__ == '__main__':
    scrape_data()