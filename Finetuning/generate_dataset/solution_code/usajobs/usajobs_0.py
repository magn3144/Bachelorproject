import csv
import requests
from bs4 import BeautifulSoup

# Load the HTML file
file_path = 'downloaded_pages/usajobs.html'
with open(file_path, 'r') as file:
    html_content = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find the desired elements using their XPaths
xpaths = [
    '/html/body/section/section/div/main/div[5]/div[11]/div[2]/div[12]/div[1]/div[2]/ul/li[3]/p',
    '/html/body/section/section/div/aside/div/div[2]/div[3]/div[2]/ul/li[1]/div/div[2]/ul/li[1]/div/ul/li/p',
    '/html/body/div[2]/div/div/div[1]',
    '/html/body/section/section/div/main/div[5]/div[13]/nav/div/a[3]/div/div',
    '/html/body/svg/symbol[1]/title',
    '/html/body/section/section/div/main/div[5]/div[11]/div[2]/div[24]/div[2]/p/svg/title',
    '/html/body/section/section/div/aside/div/div[2]/div[3]/div[1]/ul/li[4]/div/div[2]/div[2]/div[34]/ul/li[1]/label/span[1]',
    '/html/body/section/section/div/aside/div/div[2]/div[3]/div[1]/ul/li[3]/div/div[2]/section[2]/div[2]/ul[4]/li[1]/label/span[2]',
    '/html/body/section/section/div/main/div[5]/div[6]/ul/li[12]/a',
    '/html/body/section/section/div/aside/div/div[2]/div[3]/div[1]/ul/li[3]/div/div[2]/section[1]/ol/li[6]/a',
    '/html/body/section/section/div/main/div[1]/div[2]/h3',
    '/html/body/section/section/div/main/div[5]/div[10]/div/div/div/h3',
    '/html/body/section/section/div/main/div[5]/div[11]/div[2]/div[21]/div[1]/div[1]/h4[1]',
    '/html/body/section/section/div/aside/div/div[2]/div[3]/div[1]/ul/li[3]/div/div[2]/section[2]/div[2]/h4[16]',
    '/html/body/div[3]/div/div/div[2]/h2',
    '/html/body/section/section/div/main/div[5]/div[5]/h2',
    '/html/body/section/section/div/main/div[5]/div[7]/div/div/label[2]',
    '/html/body/section/section/div/aside/div/div[2]/div[3]/div[1]/ul/li[2]/div/div[2]/ul/li[3]/label',
    '/html/body/section/section/div/main/div[5]/div[11]/div[2]/div[16]/div[1]/div[1]/h5',
    '/html/body/section/section/div/aside/div/div[2]/div[3]/div[1]/ul/li[3]/div/div[2]/section[1]/h5',
    '/html/body/section/section/div/main/div[5]/div[11]/div[2]/div[8]/div[1]/div[2]/ul/li[2]',
    '/html/body/ul[2]/li[5]',
    '/html/body/div[2]/div/div/div[2]/h1',
    '/html/body/section/section/div/main/div[5]/div[11]/div[2]/div[23]/div[1]/div[2]/ul/li[3]/p',
    '/html/body/div[3]/div/div/div[1]',
    '/html/body/div[5]/div',
    '/html/body/svg/symbol[2]/title',
    '/html/body/svg/symbol[15]/title',
    '/html/body/section/section/div/aside/div/div[2]/div[3]/div[1]/ul/li[1]/div/div[2]/ul[3]/li[1]/span[1]',
    '/html/body/section/section/div/aside/div/div[2]/div[3]/div[1]/ul/li[4]/div/div[2]/div[2]/div[5]/ul/li[10]/label/span[2]',
    '/html/body/section/section/div/main/div[5]/div[6]/ul/li[8]/a',
    '/html/body/section/section/div/aside/div/div[2]/div[3]/div[1]/ul/li[4]/div/div[2]/ol/li[30]/a',
    '/html/body/section/section/div/aside/div/div[2]/div[3]/div[1]/ul/li[4]/div/div[2]/div[2]/div[19]/h4',
    '/html/body/section/section/div/aside/div/div[2]/div[3]/div[1]/ul/li[3]/div/div[2]/section[2]/div[2]/h4[13]',
    '/html/body/section/section/div/main/div[5]/div[7]/div/div/label[1]',
    '/html/body/section/section/div/aside/div/div[2]/div[3]/div[1]/ul/li[2]/div/div[2]/ul/li[2]/div/ul/li[1]/label',
    '/html/body/section/section/div/main/div[5]/div[11]/div[2]/div[17]/div[1]/div[1]/h5',
    '/html/body/section/section/div/aside/div/div[2]/div[3]/div[1]/ul/li[4]/div/div[2]/h5'
]

# Scrape the text content of the elements
scraped_data = []
for xpath in xpaths:
    element = soup.find('xpath', xpath)
    if element:
        text = element.text.strip()
    else:
        text = ''
    scraped_data.append(text)

# Save the scraped data as a CSV file
csv_file_path = 'scraped_data.csv'
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Scraped Data'])
    writer.writerows([[data] for data in scraped_data])