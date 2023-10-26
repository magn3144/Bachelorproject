from lxml import etree
import csv

def save_to_csv(data):
    keys = data[0].keys()
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

def extract_information(tree):
    data = []
    addresses = tree.xpath('//span[contains(@class, "collapsedAddress")]/text()')
    prices = tree.xpath('//div[contains(@class, "font-size-small")]/text()')
    stats = tree.xpath('//div[contains(@class, "stats")]/text()')

    for i in range(len(addresses)):
        row = {
            'Address': addresses[i],
            'Price': prices[i],
            'Stats': stats[i]
        }
        data.append(row)

    return data

def main():
    with open('downloaded_pages/redfin.html', 'rb') as file:
        html = file.read()

    parser = etree.HTMLParser()
    tree = etree.fromstring(html, parser)

    data = extract_information(tree)
    save_to_csv(data)

if __name__ == "__main__":
    main()