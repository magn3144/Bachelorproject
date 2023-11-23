import csv
from lxml import html
import requests


def scrape_DTU():
    with open("./downloaded_pages/DTU_entrepreneurship.html", "r") as file:
        page = file.read()

    tree = html.fromstring(page)
    
    departments_and_centres = tree.xpath(
        '/html/body/form/div[3]/footer/div[2]/div[1]/div/div[2]/nav/div[1]/div/div/div[3]//*')

    scraped_data = []
    scraped_data.extend(get_data(departments_and_centres))

    write_to_csv(scraped_data)


def get_data(elements):
    data = []
    for element in elements:
        text = element.text
        link = element.get('href')
        if text and link:
            data.append({"department name": text, "link": link})
    return data


def write_to_csv(data):
    keys = data[0].keys()
    with open('scraped_data.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)


scrape_DTU()