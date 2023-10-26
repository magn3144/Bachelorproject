from bs4 import BeautifulSoup
import csv

# specify the local path to the HTML file
html_file_path = 'downloaded_pages/bodybuilding.html'

# specify the XPaths of the plan elements
plan_xpaths = [
    '/html/body/section/main/div[3]/div[2]/div/div/div/div/div[2]/div/div[29]/figure/a/figcaption/div[1]/span',
    '/html/body/section/main/div[3]/div[2]/div/div/div/div/div[2]/div/div[32]/figure/a/figcaption/div[2]/span[2]',
    '/html/body/section/main/div[4]/div[2]/div/div/div/div/div[2]/div/div[5]/figure/a/figcaption/div[1]/span',
    '/html/body/section/main/div[4]/div[2]/div/div/div/div/div[2]/div/div[21]/figure/a/figcaption/div[2]/span[2]',
    '/html/body/section/main/div[5]/div[2]/div/div/div/div/div[2]/div/div[31]/figure/a/figcaption/div[1]/span',
    '/html/body/section/main/div[5]/div[2]/div/div/div/div/div[2]/div/div[22]/figure/a/figcaption/div[1]/span',
    '/html/body/section/main/div[6]/div[2]/div/div/div/div/div[2]/div/div[6]/figure/a/figcaption/div[2]/span[3]',
    '/html/body/section/main/div[4]/div[2]/div/div/div/div/div[2]/div/div[18]/figure/a/figcaption/div[1]/span'
]

# parse the HTML file
with open(html_file_path) as file:
    soup = BeautifulSoup(file, 'html.parser')

# scrape the plan tags and their corresponding XPaths
scraped_data = []
for xpath in plan_xpaths:
    elements = soup.select(xpath)
    if elements:
        plan_tag = elements[0].text.strip()
        scraped_data.append({'plan_tag': plan_tag, 'xpath': xpath})

# save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    fieldnames = ['plan_tag', 'xpath']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(scraped_data)