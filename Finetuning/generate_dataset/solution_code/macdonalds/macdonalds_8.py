import csv
from lxml import etree

# Define the local path to the HTML file
html_file = 'downloaded_pages/macdonalds.html'

# Define the XPaths for the links within the specific navigation submenu
xpaths = ['/html/body/div/div/div/header/div/div/div/div/div/div/div/div[2]/div/div[2]/div/nav/ul/li[1]/div/div/div/div/div[2]/a',
          '/html/body/div/div/div/header/div/div/div/div/div/div/div/div[2]/div/div[2]/div/nav/ul/li[3]/a',
          '/html/body/div/div/div/footer/div/div/div/div/div/div[1]/div/nav[2]/div/div/div[2]/div/div/ul/li[1]/a/span',
          '/html/body/div/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/nav/ul[2]/li[8]/a/span',
          '/html/body/div/div/div/header/div/div/div/div/div/div/div/div[1]/div[3]/div[2]/nav/ul/li[5]/a',
          '/html/body/div/div/div/header/div/div/div/div/div/div/div/div[1]/div[3]/div[2]/nav/ul/li[1]/div/div/div/div/ul/li[9]/a/span',
          '/html/body/div/div/div/header/div/div/div/div/div/div/div/div[1]/div[3]/div[2]/nav/ul/li[1]/div/div/div/div/ul/li[4]/a/span',
          '/html/body/div/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/section/div[3]/ul/li[2]/a/div/div/div[2]',
          '/html/body/div/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/section/div[3]/ul/li[5]/a/div/div/div[1]',
          '/html/body/div/div/div/footer/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/h2',
          '/html/body/div/div/div/footer/div/div/div/div/div/div[1]/div/nav[1]/ul/li[3]/div[1]/h2',
          '/html/body/div/div/div/footer/div/div/div/div/div/div[1]/div/nav[1]/ul/li[1]/div[2]/div/ul/li[3]/a/span',
          '/html/body/div/div/div/main/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div/div/div/section/div[3]/ul/li[1]/a/div/div/div[2]',
          '/html/body/div/div/div/footer/div/div/div/div/div/div[1]/div/div/div[3]/div[2]/div[2]/div/p',
          '/html/body/div/div/div/footer/div/div/div/div/div/div[1]/div/div/div[1]/div[1]/div[6]',
          '/html/body/div/div/div/footer/div/div/div/div/div/div[1]/div/nav[1]/ul/li[4]/div[1]/h2',
          '/html/body/div/div/div/header/div/div/div/div/div/div/div/div[1]/div[3]/div[1]/ul/li/a/span']

# Initialize the scraped data list
scraped_data = []

# Parse the HTML file
tree = etree.parse(html_file)

# Scrape the text from the links using the XPaths
for xpath in xpaths:
    element = tree.xpath(xpath)
    if element:
        scraped_data.append(element[0].text.strip())
    else:
        scraped_data.append('')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Link Text'])
    writer.writerows(zip(scraped_data))