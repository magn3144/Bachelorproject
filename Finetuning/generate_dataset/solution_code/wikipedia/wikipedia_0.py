import csv
from lxml import etree

def extract_statistics(html_path):
    tree = etree.parse(html_path)
    root = tree.getroot()

    statistics = []
    for element, xpath in elements.items():
        try:
            target_element = root.xpath(xpath)[0]
            statistics.append({
                'Element': element,
                'Text': target_element.text
            })
        except IndexError:
            pass

    return statistics

def save_to_csv(data, output_file):
    fieldnames = ['Element', 'Text']
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == '__main__':
    elements = {
        '<a>anniversary of the establishment of Republic of Tu</a>': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[3]/div/p/a[2]',
        '<a>Statistics</a>': '/html/body/div[2]/div/div[4]/footer/ul[2]/li[7]/a',
        '<span class="mw-headline" id="From_today\'s_featured_list">From today\'s featured list</span>': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[3]/h2/span[2]',
        '<span>Dansk</span>': '/html/body/div[2]/div/div[3]/main/div[3]/div[5]/div/div/ul/li[7]/a/span',
        '<div class="noprint" id="siteSub">From Wikipedia, the free encyclopedia</div>': '/html/body/div[2]/div/div[3]/main/div[3]/div[1]/div',
        '<div class="wikipedia-languages-count">1,000,000+ articles</div>': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[5]/div[3]/div/ul/li[1]/div[1]/div[2]',
        '<a>Twenty sculptures were erected</a>': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[3]/div/p/b[1]/a',
        '<a>6,736,355</a> articles in': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]',
        '<span>Toggle limited content width</span>': '/html/body/div[3]/ul/li/button/span[2]',
        '<span class="autonym">Lietuvių</span>': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[5]/div[3]/div/ul/li[3]/div[2]/ul/li[14]/a/span',
        '<div class="thumbcaption">Monument to the Gozo luzzu disaster</div>': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div',
        '<div class="vector-pinnable-header-label">Tools</div>': '/html/body/div[2]/div/div[3]/main/div[1]/div/div[2]/nav[2]/div/div/div/div/div[1]/div',
        '<a>Kamchatka Peninsula</a> in Russia.': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[4]/div/table/tbody/tr/td[2]/p[1]/a[6]',
        '<a>encyclopedia</a> that': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[2]/a[2]',
        '<span class="mw-headline" id="From_today\'s_featured_article">From today\'s featured article</span>': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[2]/div[1]/h2[1]/span[2]',
        '<span class="autonym">ไทย</span>': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[5]/div[3]/div/ul/li[3]/div[2]/ul/li[22]/a/span',
        '<div class="vector-menu-heading">		In other projects	</div>': '/html/body/div[2]/div/div[3]/main/div[1]/div/div[2]/nav[2]/div/div/div/div/div[5]/div[1]',
        '<a>Wikimedia Foundation, Inc.</a>, a non-profit organization.': '/html/body/div[2]/div/div[4]/footer/ul[1]/li[2]/a[5]',
        '<a>anyone can edit</a>.': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[2]/a[3]',
        '<span>Srpskohrvatski / српскохрватски</span>': '/html/body/div[2]/div/div[3]/main/div[3]/div[5]/div/div/ul/li[40]/a/span',
        '<span>Upload file</span>': '/html/body/div[1]/header/div[1]/nav/div/div/div/div/div[3]/div[2]/ul/li[5]/a/span',
        '<div class="vector-menu-heading">		Print/export	</div>': '/html/body/div[2]/div/div[3]/main/div[1]/div/div[2]/nav[2]/div/div/div/div/div[4]/div[1]',
        '<a>One dramatic specimen</a> preserves a': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[2]/div[1]/div[1]/p/a[9]',
        '<a>Archive</a>': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/ul/li[1]/b/a',
        '<span class="mw-headline" id="Wikipedia\'s_sister_projects">Wikipedia\'s sister projects</span>': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[5]/h2[2]/span[2]',
        '<span>Contents</span>': '/html/body/div[1]/header/div[1]/nav/div/div/div/div/div[2]/div[2]/ul/li[2]/a/span',
        '<div class="vector-menu-heading">		Navigation	</div>': '/html/body/div[1]/header/div[1]/nav/div/div/div/div/div[2]/div[1]',
        '<a>Georgiana, Duchess of Devonshire</a>, and': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[2]/div[1]/div[2]/ul/li[1]/a[1]',
        '<a class="extiw">Wikivoyage</a>': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[5]/div[2]/div/ul/li[11]/div[2]/span/a',
        '<span>Wikimedia Outreach</span>': '/html/body/div[2]/div/div[3]/main/div[1]/div/div[2]/nav[2]/div/div/div/div/div[5]/div[2]/ul/li[5]/a/span',
        '<div class="wikipedia-languages-count">250,000+ articles</div>': '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[5]/div[3]/div/ul/li[2]/div[1]/div[2]',
        '<a>burning coal deposits</a> as well. They can be black or multicoloured