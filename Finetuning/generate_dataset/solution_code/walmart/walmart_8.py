import csv
from lxml import html

# Define the XPaths for the berries
berrie_xpath = [
    '/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[1]/div/div/section[2]/ul/li[1]/ul/li[5]/a',
    '/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[1]/div/div/section[2]/ul/li[2]/ul/li[4]/a',
    '/html/body/div/div[1]/div/div/div[2]/div/div/main/div[1]/div[2]/div/div[2]/div/div/div[5]/section/section/div/ul/li[6]/div/a/span/h3',
]

# Parse the HTML file
with open('downloaded_pages/walmart.html', 'r') as f:
    html_content = f.read()
tree = html.fromstring(html_content)

# Scrape the berrie names and descriptions
data = []
for xpath in berrie_xpath:
    element = tree.xpath(xpath)
    if element:
        berrie_name = element[0].text_content().strip()
        berrie_description = element[0].get('class')
        data.append([berrie_name, berrie_description])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Description'])
    writer.writerows(data)