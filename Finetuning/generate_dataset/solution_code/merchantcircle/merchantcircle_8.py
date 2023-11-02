import csv
from lxml import html

def get_text(element):
    if element is not None:
        return element.text.strip()
    return ''

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Business Name', 'Phone Number'])
        writer.writerows(data)

def scrape_merchantcircle():
    html_file = 'downloaded_pages/merchantcircle.html'
    tree = html.parse(html_file)
    root = tree.getroot()

    businesses = []
    section_xpath = '//*[@class="section-class"]' # replace with the actual section class XPath
    section = root.xpath(section_xpath)
    if section:
        business_xpath = './/*[@class="business-class"]' # replace with the actual business class XPath
        for business in section[0].xpath(business_xpath):
            name_xpath = './/span[@class="business-name"]' # replace with the actual name class XPath
            name = get_text(business.xpath(name_xpath)[0])

            phone_xpath = './/span[@class="phone-number"]' # replace with the actual phone number class XPath
            phone = get_text(business.xpath(phone_xpath)[0])

            businesses.append([name, phone])

    save_to_csv(businesses)

scrape_merchantcircle()