import csv
from lxml import html
import os

def save_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def scrape_newsletters(html_content):
    tree = html.fromstring(html_content)
    newsletters = tree.xpath('/html/body/form/div[3]/footer/div[1]/div/div[4]/div[2]/h2')
    newsletter_data = []
    for newsletter in newsletters:
        data = {
            "Newsletter": newsletter.text_content().strip(),
            "XPath": tree.getpath(newsletter)
        }
        newsletter_data.append(data)
    return newsletter_data

def main():
    with open('downloaded_pages/DTU-entrepreneurship.html', 'r') as file:
        content = file.read()
    newsletters = scrape_newsletters(content)
    save_to_csv(newsletters, 'scraped_data.csv')

if __name__ == '__main__':
    main()