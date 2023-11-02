import csv
from lxml import html

def extract_melons_info(html_file):
    with open(html_file, 'r') as file:
        page_content = file.read()

    tree = html.fromstring(page_content)

    melons = tree.xpath('//h3[contains(., "melon") or contains(., "Melon")]')

    data = []
    for melon in melons:
        name = melon.text
        price_element = melon.xpath('./following-sibling::div[@class="mr1 mr2-xl b black lh-copy f5 f4-l"]')
        if price_element:
            price = price_element[0].text
        else:
            price = 'N/A'
        data.append({'Name': name, 'Price': price})

    return data

def save_data_csv(data):
    keys = data[0].keys()
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, keys)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    html_file = 'downloaded_pages/walmart.html'
    melons_info = extract_melons_info(html_file)
    save_data_csv(melons_info)