import csv
from lxml import html

def extract_navigation_info(tree, xpath):
    elements = tree.xpath(xpath)
    return [element.text.strip() for element in elements]

def save_data_to_csv(data):
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Navigation Information'])
        writer.writerows(data)

def main():
    page_path = 'downloaded_pages/careerbuilder.html'
    category = 'Jobs'
    xpaths = [
        '/html/body/div[1]/div/header/div/nav/div[2]/div/ul/li/a/span',
        '/html/body/div[1]/div/div[2]/footer/div[2]/div/div/div/div[2]/div[3]/h3',
        '/html/body/div[1]/div/div[2]/footer/div[2]/div/div/div/div[1]/div/div[2]/h3/span',
        '/html/body/div[1]/div/div[2]/footer/div[2]/div/div/div/div[2]/h3',
        '/html/body/div[1]/div/div[2]/footer/div[2]/div/div/div/div[1]/div/div[4]/div/ul/li/a'
    ]

    with open(page_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    tree = html.fromstring(html_content)

    data = []
    for xpath in xpaths:
        navigation_info = extract_navigation_info(tree, xpath)
        if navigation_info:
            data.append(navigation_info)

    save_data_to_csv(data)

if __name__ == '__main__':
    main()