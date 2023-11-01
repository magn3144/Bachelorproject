import csv
from lxml import etree

def scrape_html(html_file_path, xpath):
    tree = etree.parse(html_file_path)
    element = tree.xpath(xpath)[0]
    return element.text.strip()

def main():
    html_file_path = 'downloaded_pages/elgiganten.html'
    xpath = '/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/elk-component-loader-wrapper/elk-footer/footer/elk-lib-icon-bar/div/div[4]/a/div/div'
    scraped_data = scrape_html(html_file_path, xpath)
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([scraped_data])

if __name__ == '__main__':
    main()