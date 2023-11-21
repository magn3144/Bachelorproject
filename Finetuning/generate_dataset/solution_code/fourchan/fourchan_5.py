import csv
from html.parser import HTMLParser

class TrademarkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = []
        
    def handle_data(self, data):
        self.data.append(data)
        
    def handle_entityref(self, name):
        self.data.append('&{};'.format(name))
        
    def handle_charref(self, name):
        self.data.append('&#{};'.format(name))

def parse_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    parser = TrademarkParser()
    parser.feed(html_content)
    return parser.data

def extract_trademarks(categorized_elements):
    trademarks = []
    for element, _ in categorized_elements:
        if 'trademark' in element.lower() or 'copyright' in element.lower():
            trademarks.append(element.strip())
    return trademarks

def save_to_csv(trademarks):
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Trademark or Copyright'])
        writer.writerows([[trademark] for trademark in trademarks])

categorized_elements = [
    ('/bant/ - International/Random', '/html/body/form/table[2]/tbody/tr[2]/td[2]/a'),
    ('jp', '/html/body/div[1]/div[1]/span[1]/a[33]'),
    ('/o/ - Auto', '/html/body/div[2]/div[2]'),
    ('Your web browser must have JavaScript enabled', '/html/body/noscript/div/span'),
    ('Top', '/html/body/div[8]/span[1]/span[3]/span'),
    ('10/04/16', '/html/body/form/table[2]/tbody/tr[3]/td[1]'),
    ('Janitor acceptance emails will be sent out', '/html/body/div[5]/h4'),
    ('/vip/ - Very Important Posts', '/html/body/form/table[2]/tbody/tr[3]/td[2]/a'),
    ('po', '/html/body/div[1]/div[1]/span[1]/a[40]'),
    ('All trademarks and copyrights on this page', '/html/body/div[9]/span'),
    ('Bottom', '/html/body/div[8]/div[1]/div[1]/span[1]/span[3]/span'),
    ('Options', '/html/body/form/table[1]/tbody/tr[2]/td[1]'),
    ('Disable Mobile View / Use Desktop Site', '/html/body/div[9]/div[1]/span[1]/a'),
    ('Show', '/html/body/div[8]/span[3]/span[2]/a'),
    ('Start a New Thread', '/html/body/div[3]/span/span'),
    ('Subject', '/html/body/form/table[1]/tbody/tr[3]/td[1]'),
    ('Enable Mobile View / Use Mobile Site', '/html/body/div[9]/div[1]/span[2]/a'),
    ('fa', '/html/body/div[1]/div[1]/span[1]/a[28]'),
    ('🎉', '/html/body/div[5]/h2/span[2]'),
    ('05/04/17', '/html/body/form/table[2]/tbody/tr[2]/td[1]'),
    ('Feedback', '/html/body/div[9]/div[2]/a[2]'),
    ('✖', '/html/body/div[8]/div[1]/div[2]/span[6]/span'),
    ('File', '/html/body/form/table[1]/tbody/tr[6]/td[1]'),
    ('v', '/html/body/div[1]/div[1]/span[1]/a[8]')
]

html_file_path = 'downloaded_pages/4chan.html'
categorized_elements_xpath = [element[1] for element in categorized_elements]
html_data = parse_html_file(html_file_path)

categorized_elements_data = list(zip(html_data, categorized_elements_xpath))
trademarks = extract_trademarks(categorized_elements_data)
save_to_csv(trademarks)