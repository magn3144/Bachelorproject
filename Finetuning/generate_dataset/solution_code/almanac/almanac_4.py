import csv
from lxml import etree


def extract_data(element, xpath):
    try:
        data = element.xpath(xpath)[0].text
    except:
        data = ''
    return data

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Price'])
        for item in data:
            writer.writerow(item)


# Load the HTML file
with open('downloaded_pages/almanac.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Parse the HTML
parser = etree.HTMLParser(remove_blank_text=True)
tree = etree.parse('<html><body>' + html + '</body></html>', parser)

# Extract and save the names and prices of gardening books
data = []
elements = tree.xpath('//p[@class="prod-title"] | //p[contains(@class, "price")]')
for i in range(0, len(elements), 2):
    name = extract_data(elements[i], '.')
    price = extract_data(elements[i+1], '.')
    data.append([name, price])

save_to_csv(data)