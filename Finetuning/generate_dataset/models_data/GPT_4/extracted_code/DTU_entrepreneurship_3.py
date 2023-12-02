import csv
from lxml import html
from os.path import join

def scrape_buttons():
    file_path = join('downloaded_pages', 'DTU_entrepreneurship.html')
    page_content = open(file_path, 'r').read()
    tree = html.fromstring(page_content)

    header_button_paths = tree.xpath('//div[@class="header"]/button')
    buttons_text = [button.text_content().strip() for button in header_button_paths]

    with open('scraped_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['Button Text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for button in buttons_text:
            writer.writerow({'Button Text': button})
            
if __name__ == "__main__":
    scrape_buttons()