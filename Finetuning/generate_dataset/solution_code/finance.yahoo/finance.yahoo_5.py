import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/finance.yahoo.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Define the XPaths of the elements to scrape
xpaths = {
    'element1': '/html/body/div[1]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/ul/li[13]/a',
    'element2': '/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/ul/li[2]/a',
    'element3': '/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div/form/label',
    'element4': '/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/ul/li[2]/div/div/div/div[2]/ul/li[29]/a/div/div/p',
    'element5': '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/ul/li[2]/div/div[1]/div/p',
    'element6': '/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/ul/li[2]/div/div/div/h3',
    'element7': '/html/body/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div/div/div[2]/div/ul/li[4]/div/div/div/div[2]/div',
    'element8': '/html/body/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div/div/div[2]/div/ul/li[5]/div/div/div/h3/a/span',
    'element9': '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/section/div/div[2]/div[1]/table/tbody/tr[21]/td[5]/fin-streamer/span',
    'element10': '/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/ul/li[2]/div/div/div/div[1]/h4',
    'element11': '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/section/div/div[2]/div[1]/table/thead/tr/th[3]',
    'element12': '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/section/div/div[2]/div[1]/table/tbody/tr[25]/td[2]',
    'element13': '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/section/div/div[2]/div[1]/table/tbody/tr[21]/td[2]',
    'element14': '/html/body/div[1]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/ul/li[12]/a',
    'element15': '/html/body/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div/div/div[2]/div/ul/li[14]/div/div[1]/div[2]/a',
    'element16': '/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/ul/li[2]/div/div/div/div[2]/ul/li[34]/a/div/div/p',
    'element17': '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/ul/li[12]/div/div[1]/div/p',
    'element18': '/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div/form/div[2]/div[2]/div/h3',
    'element19': '/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div/form/div[2]/div[2]/ul/li[3]/div[2]',
    'element20': '/html/body/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div/div/div[2]/div/ul/li[13]/div/div/div/h3/a/span',
    'element21': '/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/ul/li[3]/a/span',
    'element22': '/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/ul/li[2]/div/div/div/div[2]/h4',
    'element23': '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/section/div/div[2]/div[1]/table/thead/tr/th[6]'
}

# Scraping the elements
scraped_data = {}
for key, xpath in xpaths.items():
    element = tree.xpath(xpath)
    scraped_data[key] = element[0].text_content().strip()

# Saving the data as a CSV file
with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Element', 'Text'])
    for key, value in scraped_data.items():
        writer.writerow([key, value])