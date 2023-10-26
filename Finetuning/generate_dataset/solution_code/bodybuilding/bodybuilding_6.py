import csv
from lxml import html

# Define the HTML file path
html_file = 'downloaded_pages/bodybuilding.html'

# Define the XPaths of the plan durations
xpaths = [
    '/html/body/section/main/div[3]/div[2]/div/div/div/div/div[2]/div/div[29]/figure/a/figcaption/div[2]/span[3]',
    '/html/body/section/main/div[3]/div[2]/div/div/div/div/div[2]/div/div[32]/figure/a/figcaption/div[2]/span[2]',
    '/html/body/section/main/div[4]/div[2]/div/div/div/div/div[2]/div/div[5]/figure/a/figcaption/div[2]/span[2]',
    '/html/body/section/main/div[4]/div[2]/div/div/div/div/div[2]/div/div[21]/figure/a/figcaption/div[2]/span[2]',
    '/html/body/section/main/div[5]/div[2]/div/div/div/div/div[2]/div/div[31]/figure/a/figcaption/div[2]/span[2]',
    '/html/body/section/main/div[6]/div[2]/div/div/div/div/div[2]/div/div[6]/figure/a/figcaption/div[2]/span[3]',
    '/html/body/section/main/div[5]/div[2]/div/div/div/div/div[2]/div/div[22]/figure/a/figcaption/div[2]/span[2]',
    '/html/body/section/main/div[7]/ul/li[2]/div/div/ul/li[15]'
]

# Scrape the plan durations
tree = html.parse(html_file)
plan_durations = [tree.xpath(xpath)[0].text_content().strip() for xpath in xpaths]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Plan Duration'])
    writer.writerows(zip(plan_durations))