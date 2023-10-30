import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/globestudios.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Parse HTML content
tree = html.fromstring(html_content)

# Define the list of web scraping tasks
tasks = [
    {
        'task': 'Get club title',
        'xpath': '/html/body/div/div[4]/footer/div[1]/div[3]/div/div[1]'
    },
    {
        'task': 'Check product drawer content',
        'xpath': '/html/body/div/div[6]/div/div[2]'
    },
    {
        'task': 'Get product title',
        'xpath': '/html/body/div/div[3]/div[2]/div/div/div/div/div[1]/div[10]/product-card/div/a'
    },
    {
        'task': 'Get menu item',
        'xpath': '/html/body/div/div[2]/header/div/div/full-menu/ul/li[2]/div/ul/li[2]/ul/li[3]/a'
    },
    {
        'task': 'Get add to cart text',
        'xpath': '/html/body/div/div[3]/div[2]/div/div/div/div/div[1]/div[4]/product-card/figure/a/quick-view/span'
    },
    {
        'task': 'Get newsletter text',
        'xpath': '/html/body/div/div[3]/div[6]/div/div/div[1]/div/div/p'
    },
    {
        'task': 'Get empty cart text',
        'xpath': '/html/body/div/div[5]/div/div[2]/div[1]/p'
    },
    {
        'task': 'Get location text',
        'xpath': '/html/body/div/div[3]/div[5]/div/div/div[1]/div[2]/h6'
    },
    {
        'task': 'Get club description',
        'xpath': '/html/body/div/div[3]/div[6]/div/div/div[1]/div/h2'
    },
    {
        'task': 'Get email label',
        'xpath': '/html/body/div/div[4]/footer/div[1]/div[3]/div/div[2]/form/fieldset/div/label'
    },
    {
        'task': 'Get title',
        'xpath': '/html/body/div/div[4]/footer/div[2]/div/div[2]/div/figure[4]/svg/title'
    },
    {
        'task': 'Get cart title',
        'xpath': '/html/body/div/div[5]/div/div[1]/div/h4'
    },
    {
        'task': 'Check side panel content',
        'xpath': '/html/body/div/div[7]/div/div[2]'
    },
    {
        'task': 'Get product title',
        'xpath': '/html/body/div/div[7]/div/div[3]/div/div[2]/div/ul/li[2]/product-card/div/a'
    },
    {
        'task': 'Get sale link',
        'xpath': '/html/body/div/div[2]/header/div/div/full-menu/ul/li[2]/div/div[2]/div/a'
    },
    {
        'task': 'Get shop link text',
        'xpath': '/html/body/div/div[3]/div[1]/div/div/div/div[2]/div[3]/div/div[2]/a/span'
    },
    {
        'task': 'Get footer text',
        'xpath': '/html/body/div/div[4]/footer/div[2]/div/div[3]/p'
    },
    {
        'task': 'Get description',
        'xpath': '/html/body/div/div[3]/div[1]/div/div/div/div[2]/div[3]/div/p'
    },
    {
        'task': 'Get location text',
        'xpath': '/html/body/div/div[3]/div[5]/div/div/div[2]/div[2]/h6'
    },
    {
        'task': 'Get search label',
        'xpath': '/html/body/div/div[7]/div/div[1]/div/form/fieldset/label'
    },
    {
        'task': 'Get product title',
        'xpath': '/html/body/div/div[3]/div[2]/div/div/div/div/div[1]/div[7]/product-card/div/a'
    },
    {
        'task': 'Get contact link',
        'xpath': '/html/body/div/div[2]/header/div/div/div[1]/details/nav/div/ul[1]/li[3]/details/ul/li[3]/a'
    },
    {
        'task': 'Get product title',
        'xpath': '/html/body/div/div[3]/div[2]/div/div/div/div/div[1]/div[2]/product-card/div/a'
    },
    {
        'task': 'Get knit link',
        'xpath': '/html/body/div/div[2]/header/div/div/div[1]/details/nav/div/ul[1]/li[2]/details/ul/li[3]/details/ul/li[3]/a'
    },
    {
        'task': 'Get product title',
        'xpath': '/html/body/div/div[3]/div[2]/div/div/div/div/div[1]/div[8]/product-card/div/a'
    },
    {
        'task': 'Get bestsellers link',
        'xpath': '/html/body/div/div[7]/div/div[3]/div/div[1]/scroll-shadow/div/a[2]'
    }
]

# Scrape the data
scraped_data = []
for task in tasks:
    result = tree.xpath(task['xpath'])
    if len(result) > 0:
        scraped_data.append((task['task'], result[0].text_content()))

# Save the scraped data as CSV
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Task', 'Data'])
    writer.writerows(scraped_data)