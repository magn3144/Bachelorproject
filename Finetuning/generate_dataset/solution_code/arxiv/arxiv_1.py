import csv
from lxml import etree

def extract_element(tree, xpath):
    element = tree.xpath(xpath)
    if element:
        return element[0].text.strip()
    else:
        return ''

def main():
    with open('downloaded_pages/arxiv.html', 'r') as f:
        html = f.read()

    tree = etree.HTML(html)

    data = []
    descriptors_xpath = [
        '/html/body/div[4]/div/dl/dd[11]/div/div[4]/span[1]',
        '/html/body/div[4]/div/dl/dd[19]/div/div[1]/span',
        '/html/body/div[4]/div/dl/dd[17]/div/div[4]/span[1]',
        '/html/body/div[4]/div/dl/dd[19]/div/div[4]/span[1]'
    ]

    for xpath in descriptors_xpath:
        descriptor = extract_element(tree, xpath)
        data.append([descriptor])

    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

if __name__ == '__main__':
    main()