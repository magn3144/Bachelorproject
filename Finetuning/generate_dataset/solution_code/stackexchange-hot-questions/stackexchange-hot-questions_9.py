from lxml import html
import csv

# XPaths for the top network askers
top_network_askers_xpaths = [
    '/html/body/div/section/div/div[3]/div[2]/div[1]/div/span',
    '/html/body/div/section/div/div[3]/div[2]/div[21]/div/span[1]/a',
    '/html/body/div/section/div/div[3]/div[2]/div[17]/div/div/span/a',
    '/html/body/div/section/div/div[3]/div[2]/div[24]/div/span[1]/a',
    '/html/body/div/section/div/div[3]/div[2]/div[14]/div/span[1]/a'
]

# Load the HTML file
with open('downloaded_pages/stackexchange-hot-questions.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Scrape the top network askers
askers = []
for xpath in top_network_askers_xpaths:
    asker = tree.xpath(xpath)
    if asker:
        askers.append(asker[0].text)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Top Network Askers'])
    writer.writerows(map(lambda x: [x], askers))

print("Data saved successfully!")