import csv
from lxml import html

# Define the local path to the HTML file
html_file = 'downloaded_pages/coolshop.html'

# Define the XPaths for the categories
xpaths = [
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[22]/section/div/div[1]/div/a',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[17]/section/div/div[1]/ul/li[10]/a',
    '/html/body/div[3]/div[1]',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[2]/div/div/div',
    '/html/body/div[1]/section[12]/p',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[32]/section/div/div[2]/div[1]/p',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[17]/section/div/div[2]/ul/li[5]/a/span',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[10]/section/div/div[4]/ul/li[4]/a/span',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[7]/section/div/div[3]/ul/li[1]',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[7]/section/div/div[4]/ul/li[12]',
    '/html/body/header/div[3]/div[2]/div/div[1]/div[1]/h6',
    '/html/body/div[1]/section[15]/h2',
    '/html/body/div[1]/section[4]/h2',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[6]/section/div/div[1]/ul/li[2]/a',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[22]/section/div/div[1]/ul/li[4]/a',
    '/html/body/div[1]/section[17]/div[2]',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[21]/div/div/div',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[22]/section/div/div[2]/div[1]/p',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[21]/section/div/div[2]/div[1]/p',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[14]/section/div/div[2]/ul/li[10]/a/span',
    '/html/body/div[1]/section[16]/div[5]/div[1]/a/span',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[6]/section/div/div[4]/ul/li[1]',
    '/html/body/footer/div[4]/div/div/div[2]/ul/li[1]',
    '/html/body/header/div[3]/div[2]/div/div[3]/div[1]/h6',
    '/html/body/div[1]/section[6]/h2',
    '/html/body/div[1]/section[5]/h2',
    '/html/body/footer/div[2]/div/div[2]/span/a',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[15]/section/div/div[3]/ul/li[12]/a',
    '/html/body/footer/div[2]/div/div[4]',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[4]/div/a/div[2]',
    '/html/body/div[1]/section[9]/p',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[20]/section/div/div[4]/div[1]/p',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[21]/section/div/div[2]/ul/li[10]/a/span',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[10]/section/div/div[2]/ul/li[5]/a/span',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[7]/section/div/div[4]/ul/li[1]',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[24]/section/div/div[1]/ul/li[9]',
    '/html/body/header/div[3]/div[2]/div/div[2]/div[1]/h6',
    '/html/body/div[1]/section[12]/h2',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[15]/section/div/div[1]/ul/li[9]/a',
    '/html/body/header/div[1]/div[2]/div[2]/div[1]/nav/div[2]/ul/li[21]/section/div/div[1]/ul/li[1]/a',
    '/html/body/footer/div[2]/div/div[2]/div[1]'
]

# Scrape the categories from the HTML file using the XPaths
categories = []
tree = html.parse(html_file)
for xpath in xpaths:
    category = tree.xpath(xpath)[0].text
    categories.append(category)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Categories'])
    for category in categories:
        writer.writerow([category])