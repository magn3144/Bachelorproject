import csv
import requests
from lxml import html


def scrape_website(html_path, xpath_list):
    with open(html_path, 'r') as file:
        webpage = file.read()

    tree = html.fromstring(webpage)

    industry_names = []
    for xpath in xpath_list:
        elements = tree.xpath(xpath)
        for element in elements:
            if element.text:
                industry_names.append(element.text.strip())

    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Industry Name'])
        for industry in industry_names:
            writer.writerow([industry])


if __name__ == "__main__":
    html_path = 'downloaded_pages/finviz.html'
    xpath_list = [
        '/html/body/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/table/tbody/tr/td/table/thead/tr/th[5]',
        '/html/body/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[2]/td[4]/a',
        '/html/body/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[5]/td[5]/a',
        '/html/body/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[16]/td[5]/a',
        '/html/body/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[15]/td[4]/a',
        '/html/body/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[15]/td[3]/a',
        '/html/body/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[14]/td[9]/a/span',
        '/html/body/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[11]/td[2]/a',
        '/html/body/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[20]/td[10]/a/span',
        '/html/body/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[4]/td[3]/a',
        '/html/body/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr[7]/td[3]/a'
    ]

    scrape_website(html_path, xpath_list)