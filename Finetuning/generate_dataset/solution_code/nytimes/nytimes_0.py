import csv
from lxml import html

def scrape_page(category, elements, path):
    scraped_data = []
    with open(path, 'r') as file:
        content = file.read()
        tree = html.fromstring(content)

        for element, xpath in elements.items():
            text = tree.xpath(xpath)
            if text:
                scraped_data.append((element, text[0].text_content()))
            else:
                scraped_data.append((element, "N/A"))

    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Category', 'Element', 'Text'])

        for element, text in scraped_data:
            writer.writerow([category, element, text])

# Category: News
category = 'News'

# HTML elements and their XPaths
elements = {
    'Element 1': '/html/body/div/div[2]/main/section/div[1]/section[2]/ol/li[2]/div/div/p[1]/a',
    'Element 2': '/html/body/div/div[2]/nav/div/div[2]/div/section[5]/ul/li[5]/a',
    'Element 3': '/html/body/div/div[2]/main/section/div[1]/section[2]/ol/li[5]/div/figure/figcaption/span/span',
    'Element 4': '/html/body/div/div[2]/main/section/div[2]/div/section/div[1]/ol/li[5]/div/div/span',
    'Element 5': '/html/body/div/div[2]/main/section/div[1]/section[1]/div[2]/div/ol/li[1]/div/div/p[2]',
    'Element 6': '/html/body/div/div[2]/main/section/header/div/div[1]/div/div/div[1]/p',
    'Element 7': '/html/body/div/div[2]/main/section/header/div/div[2]/div/div/h1',
    'Element 8': '/html/body/div/div[2]/footer/nav/h2',
    'Element 9': '/html/body/div/div[2]/main/section/div[1]/section[1]/div[1]/h2',
    'Element 10': '/html/body/div/div[2]/main/section/div[2]/div/nav/ul/li[2]/a/form/div/div[1]/label',
    'Element 11': '/html/body/div/div[2]/main/section/div[2]/div/section/div[1]/ol/li[1]/div/article/a/h3',
    'Element 12': '/html/body/div/div[2]/nav/div/div[2]/div/section[3]/h3',
    'Element 13': '/html/body/div/div[2]/main/section/div[1]/section[1]/div[1]/ol/li[1]/article/div/h3/a',
    'Element 14': '/html/body/div/div[2]/nav/div/div[1]/div/div[5]/div/ul/li[10]/a',
    'Element 15': '/html/body/div/div[2]/main/section/div[1]/section[1]/div[1]/ol/li[3]/ol/li[1]/article/figure/figcaption/span/span',
    'Element 16': '/html/body/div/div[2]/main/section/div[2]/div/section/div[1]/ol/li[9]/div/article/div[2]/p/span',
    'Element 17': '/html/body/div/div[2]/main/section/div[2]/div/section/div[1]/ol/li[1]/div/article/p',
    'Element 18': '/html/body/div/div[2]/main/section/div[2]/div/section/div[2]/div[1]/div[1]/p',
    'Element 19': '/html/body/div/div[2]/main/section/div[2]/div/section/div[2]/aside/header/h2',
    'Element 20': '/html/body/div/div[2]/main/section/div[2]/div/section/div[1]/ol/li[6]/div/article/a/h3',
    'Element 21': '/html/body/div/div[2]/nav/div/div[2]/div/section[4]/h3',
    'Element 22': '/html/body/div/div[2]/main/section/div[1]/section[2]/ol/li[1]/div/div/p[1]/a',
    'Element 23': '/html/body/div/div[2]/nav/div/div[1]/div/div[3]/div/ul/li[3]/a',
    'Element 24': '/html/body/div/div[2]/main/section/div[1]/section[1]/div[1]/ol/li[3]/ol/li[2]/article/figure/figcaption/span/span',
    'Element 25': '/html/body/div/div[2]/main/section/div[2]/div/section/div[1]/ol/li[6]/div/div/span',
    'Element 26': '/html/body/div/div[2]/main/section/div[1]/section[2]/ol/li[1]/div/div/p[2]',
    'Element 27': '/html/body/div/div[2]/main/section/div[1]/div/div[1]/p',
    'Element 28': '/html/body/div/div[2]/nav/h2',
    'Element 29': '/html/body/div/div[2]/main/section/div[2]/div/section/div[1]/ol/li[5]/div/article/a/h3',
    'Element 30': '/html/body/div/div[2]/nav/div/div[2]/div/section[1]/h3',
    'Element 31': '/html/body/div/div[2]/main/section/div[1]/section[1]/div[2]/div/ol/li[4]/div/div/p[1]/a',
    'Element 32': '/html/body/div/div[2]/nav/div/div[1]/div/div[5]/div/ul/li[3]/a',
    'Element 33': '/html/body/div/div[2]/main/section/div[1]/section[1]/div[2]/div/ol/li[4]/div/div/p[3]/span[3]/span',
    'Element 34': '/html/body/div/div[1]/div/header/section[1]/div[1]/div[2]/button/span',
    'Element 35': '/html/body/div/div[2]/main/section/div[1]/section[2]/ol/li[3]/div/div/p[2]',
    'Element 36': '/html/body/div/div[2]/main/section/div[2]/div/section/div[2]/div[2]/div[1]/p',
    'Element 37': '/html/body/div/div[2]/main/section/div[2]/div/section/div[1]/ol/li[2]/div/article/a/h3',
    'Element 38': '/html/body/div/div[2]/nav/div/div[2]/div/div/h3',
    'Element 39': '/html/body/div/div[2]/main/section/div[1]/section[1]/div[2]/div/ol/li[1]/div/div/p[1]/a',
    'Element 40': '/html/body/div/div[2]/nav/div/div[1]/div/div[5]/div/ul/li[3]/a',
    'Element 41': '/html/body/div/div[2]/main/section/div[1]/section[1]/div[2]/div/ol/li[4]/div/div/p[3]/span[3]/span',
    'Element 42': '/html/body/div/div[1]/div/header/section[1]/div[1]/div[2]/button/span',
    'Element 43': '/html/body/div/div[2]/main/section/div[1]/section[2]/ol/li[3]/div/div/p[2]',
    'Element 44': '/html/body/div/div[2]/main/section/div[2]/div/section/div[2]/div[2]/div[1]/p',
    'Element 45': '/html/body/div/div[2]/main/section/div[2]/div/section/div[1]/ol/li[2]/div/article/a/h3',
    'Element 46': '/html/body/div/div[2]/nav/div/div[2]/div/div/h3',
    'Element 47': '/html/body/div/div[2]/main/section/div[1]/section[1]/div[2]/div/ol/li[1]/div/div/p[1]/a',
    'Element 48': '/html/body/div/div[2]/nav/div/div[1]/div/div[5]/div/ul/li[3]/a',
    'Element 49