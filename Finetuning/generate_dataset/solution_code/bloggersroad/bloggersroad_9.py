import csv
from lxml import etree

# Define the target HTML file path
html_file_path = 'downloaded_pages/bloggersroad.html'

# Define the web-scraping task
task = 'Scrape the links for the best classifieds in different cities and their XPaths'

# Define the HTML elements and their XPaths
elements = [
    {'element': '<a>Best Free Classifieds in Henderson, Nevada</a>', 'xpath': '/html/body/div/div[1]/div/main/div/article[3]/div/header/h2/a'},
    {'element': '<a>Craigslist Alternative Classifieds in Greensboro, </a>', 'xpath': '/html/body/div/div[1]/div/main/div/article[4]/div/header/h2/a'},
    {'element': '<a>Top 12 Online Classifieds in Great Falls, Montana</a>', 'xpath': '/html/body/div/div[1]/section/section[4]/ul/li[5]/a'}
]

# Scrape the links and their XPaths from the HTML file
links_and_xpaths = []
with open(html_file_path, 'r') as file:
    html = file.read()
    
    for element in elements:
        try:
            tree = etree.HTML(html)
            link = tree.xpath(element['xpath'])[0].text
            xpath = element['xpath']
            links_and_xpaths.append({'link': link, 'xpath': xpath})
        except:
            continue

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['link', 'xpath'])
    writer.writeheader()
    writer.writerows(links_and_xpaths)