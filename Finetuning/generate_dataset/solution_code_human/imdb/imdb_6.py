import csv
from lxml import html
from os.path import join, dirname, realpath

def save_to_file(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def scrape():
    file_path = join('downloaded_pages', 'imdb.html')
    parser = html.HTMLParser(encoding='utf-8')
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = html.parse(file, parser=parser)

    # Get the links
    links = []
    link_elems = []
    for i in range(2, 9):
        links_xpath = f'//*[@id="__next"]/main/div/div[3]/section/div/div[2]/section/div[4]/div[{i}]/a'
        link_elems.append(tree.xpath(links_xpath))
        links.append(link_elems[-1][0].get('href'))

    # For each link element get the h3 text
    h3texts = []
    for link in link_elems:
        h3text = link[0].xpath('.//h3/text()')[0]
        h3texts.append(h3text)

    data = []
    for i in range(len(h3texts)):
        data.append([h3texts[i], links[i]])
    save_to_file(data)


scrape()