import csv
from lxml import etree


def extract_number_of_divorces(html):
    parser = etree.HTMLParser()
    tree = etree.parse(html, parser)
    
    xpath = "/html/body/div[1]/main/div/div[2]/div[1]/div/div/div[3]/div[2]/div/div[2]/div[2]/a"
    element = tree.xpath(xpath)
    
    if element:
        text = element[0].text
        number_of_divorces = ''.join(c for c in text if c.isdigit())
        return number_of_divorces

    return None


def save_data_as_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Number of Divorces'])
        writer.writerow([data])


if __name__ == '__main__':
    html_file = 'downloaded_pages/dst.html'
    scraped_data = extract_number_of_divorces(html_file)
    if scraped_data:
        save_data_as_csv(scraped_data, 'scraped_data.csv')