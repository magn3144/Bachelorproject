import csv
from lxml import etree

def get_text(element):
    return element.text.strip() if element is not None else ''

def get_element_text_from_xpath(root, xpath):
    element = root.xpath(xpath)
    return get_text(element[0]) if len(element) > 0 else ''

def scrape_data():
    # Load the HTML file
    with open('downloaded_pages/boardgamegeek.html', 'r') as file:
        html = file.read()

    # Parse the HTML
    parser = etree.HTMLParser()
    root = etree.fromstring(html, parser)

    # Find all forum listings in the "Forums and Review Sites" category
    forum_listings = root.xpath('/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/div/gg-forum-listings/gg-forum-section-list[10]/section/ul/li/gg-forum-listing')
    
    data = []
    
    # Extract names and locations of forums
    for listing in forum_listings:
        name_xpath = './/a[contains(@class, "dropdown-item")]'
        location_xpath = './/a[contains(@class, "dropdown-item")]/text()'

        name = get_element_text_from_xpath(listing, name_xpath)
        location = get_element_text_from_xpath(listing, location_xpath)

        data.append([name, location])

    # Save the scraped data as CSV
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Location'])
        writer.writerows(data)

if __name__ == "__main__":
    scrape_data()