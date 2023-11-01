import csv
from lxml import etree

def get_song_names(html_file):
    parser = etree.HTMLParser()
    tree = etree.parse(html_file, parser)

    song_names = tree.xpath('//h2[contains(text(),"You\'re now in slide show mode.")]/following-sibling::ul[1]/li//h2/a/text()')
    
    return song_names

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Song Name'])
        writer.writerows(data)

html_file = 'downloaded_pages/myspace.html'
song_names = get_song_names(html_file)
save_to_csv(song_names)