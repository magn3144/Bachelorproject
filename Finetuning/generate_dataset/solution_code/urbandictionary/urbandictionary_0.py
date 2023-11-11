import csv
from lxml import html

def scrape_page(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    tree = html.fromstring(content)
    rows = []
    
    for element in html_elements:
        xpath = html_elements[element]
        data = tree.xpath(xpath)
        
        if data:
            row = [element, data[0].text_content()]
            rows.append(row)
    
    return rows

def save_data(data):
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Element', 'Definition'])
        writer.writerows(data)

html_elements = {
    'data subject access request': '/html/body/div/div/main/div/div[4]/aside/div[2]/div[2]/ul/li[9]/a',
    'Advertise': '/html/body/div/header/div[2]/div[1]/div/div/ul/li[5]/a',
    'bald head thunder fuck': '/html/body/div/div/main/div/div[4]/section/div[4]/a/span',
    'Flag': '/html/body/div/div/main/div/div[4]/section/div[3]/div/div[5]/a/span',
    '© 1999-2023 Urban Dictionary ®': '/html/body/div/div/main/div/div[4]/aside/div[2]/div[2]/div',
    'msgrumpy': '/html/body/div/div/main/div/div[4]/section/div[1]/div/div[4]/a',
    'H': '/html/body/div/header/div[2]/div[1]/div/div/ul/li[1]/div/div/ul/li[8]/a',
    'Define a Word': '/html/body/div/div/main/div/div[4]/aside/div[1]/div/a/span',
    'I will write this on your tomb': '/html/body/div/div/main/div/div[4]/section/div[3]/div/div[4]/a',
    'Discord': '/html/body/div/header/div[2]/div[1]/div/div/ul/li[4]/a',
    'Facebook': '/html/body/div/div/main/div/div[4]/aside/div[1]/ul/li[2]/a/span',
    'Ghetto Baby Gurl': '/html/body/div/div/main/div/div[4]/section/div[9]/div/div[2]/a[1]',
    'V': '/html/body/div/header/div[2]/div[1]/div/div/ul/li[1]/div/div/ul/li[22]/a',
    '0': '/html/body/div/div/main/div/div[4]/section/div[4]/div/div[5]/div/button[2]/span',
    'cursive': '/html/body/div/div/main/div/div[4]/section/div[9]/div/div[2]/a[2]',
    'is nice': '/html/body/div/div/main/div/div[4]/section/div[6]/div/div[3]/a[2]',
    '0': '/html/body/div/div/main/div/div[4]/section/div[6]/div/div[5]/div/button[2]/span',
    'information collection notice': '/html/body/div/div/main/div/div[4]/aside/div[2]/div[2]/ul/li[8]/a',
    'ads': '/html/body/div/div/main/div/div[4]/aside/div[2]/div[2]/ul/li[1]/a',
    '0': '/html/body/div/div/main/div/div[4]/section/div[7]/div/div[5]/div/button[1]/span',
    'gbglova': '/html/body/div/div/main/div/div[4]/section/div[9]/div/div[4]/a',
    'U': '/html/body/div/header/div[2]/div[1]/div/div/ul/li[1]/div/div/ul/li[21]/a',
    '1': '/html/body/div/div/main/div/div[4]/section/div[6]/div/div[5]/div/button[1]/span',
    'disappeared': '/html/body/div/div/main/div/div[4]/section/div[6]/div/div[2]/a[2]',
    '#': '/html/body/div/header/div[1]/div[2]/div/div/ul/li[2]/ul/li[27]/a',
    '21': '/html/body/div/div/main/div/div[4]/section/div[9]/div/div[5]/div/button[1]/span',
    'to gym': '/html/body/div/div/main/div/div[4]/section/div[9]/div/div[2]/a[3]',
    'next level': '/html/body/div/div/main/div/div[4]/section/div[10]/div/div[3]/a[3]',
    'Sus': '/html/body/div/div/main/div/div[4]/section/div[7]/a/span',
    'Meowbro': '/html/body/div/div/main/div/div[4]/section/div[10]/div/div[4]/a',
    'these days': '/html/body/div/div/main/div/div[4]/section/div[1]/div/div[2]/a[3]',
    'GBG': '/html/body/div/div/main/div/div[4]/section/div[9]/a/span',
    'a single': '/html/body/div/div/main/div/div[4]/section/div[3]/div/div[2]/a[3]',
    'W': '/html/body/div/header/div[2]/div[1]/div/div/ul/li[1]/div/div/ul/li[23]/a',
    '0': '/html/body/div/div/main/div/div[4]/section/div[7]/div/div[5]/div/button[2]/span',
    'shut the fuck up': '/html/body/div/div/main/div/div[4]/section/div[4]/div/div[3]/a[3]',
    'D': '/html/body/div/header/div[2]/div[1]/div/div/ul/li[1]/div/div/ul/li[4]/a',
    '22': '/html/body/div/div/main/div/div[4]/section/div[1]/div/div[5]/div/button[2]/span',
    'ForTehKenny': '/html/body/div/div/main/div/div[4]/section/div[4]/div/div[4]/a',
    'Dejoaq': '/html/body/div/div/main/div/div[4]/section/div[6]/div/div[1]/h2/a',
    "that's tight": '/html/body/div/div/main/div/div[4]/section/div[1]/div/div[3]/a[2]',
    'A': '/html/body/div/header/div[1]/div[2]/div/div/ul/li[2]/ul/li[1]/a'
}

data = scrape_page('downloaded_pages/urbandictionary.html')
save_data(data)