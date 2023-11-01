import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/netflix.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML
parser = etree.HTMLParser()
tree = etree.HTML(html_content)

# Define the TV programme titles and their corresponding XPaths
titles_xpaths = {
    'Into the Deep: The Submarine Murder Case': '/html/body/div[1]/div/div[2]/main/section[6]/div/ul/li[12]/span/span[2]',
    'Maybe Baby': '/html/body/div[1]/div/div[2]/main/section[5]/div/ul/li[2]/a/span[2]',
    'Lifting the Veil: Behind the Scenes of Ehrengard': '/html/body/div[1]/div/div[2]/main/section[7]/div/ul/li[13]/span/span[2]',
    'Maybe Baby': '/html/body/div[1]/div/div[2]/main/section[2]/div/ul/li[5]/a/span[2]',
    'LEGO Ninjago: Masters of Spinjitzu': '/html/body/div[1]/div/div[2]/main/section[3]/div/ul/li[2]/a/span[2]',
    'Pagten': '/html/body/div[1]/div/div[2]/main/section[2]/div/ul/li[3]/a/span[2]',
    'Copenhagen Cowboy: Nightcall with Nicolas Winding': '/html/body/div[1]/div/div[2]/main/section[4]/div/ul/li[24]/a/span[2]',
    'Empire': '/html/body/div[1]/div/div[2]/main/section[4]/div/ul/li[7]/a/span[2]',
    'Lifting the Veil: Behind the Scenes of Ehrengard': '/html/body/div[1]/div/div[2]/main/section[6]/div/ul/li[20]/span/span[2]',
    'Pagten': '/html/body/div[1]/div/div[2]/main/section[4]/div/ul/li[18]/a/span[2]',
    'Copenhagen Cowboy: Nightcall with Nicolas Winding': '/html/body/div[1]/div/div[2]/main/section[7]/div/ul/li[16]/span/span[2]',
    'A Fortunate Man': '/html/body/div[1]/div/div[2]/main/section[4]/div/ul/li[11]/a/span[2]',
    'LEGO Ninjago: Masters of Spinjitzu': '/html/body/div[1]/div/div[2]/main/section[2]/div/ul/li[8]/a/span[2]',
    'Elves': '/html/body/div[1]/div/div[2]/main/section[3]/div/ul/li[6]/a/span[2]',
    'Arn: Riket vid vägens slut': '/html/body/div[1]/div/div[2]/main/section[7]/div/ul/li[5]/span/span[2]'
}

# Prepare the data for CSV
data = []
for title, xpath in titles_xpaths.items():
    element = tree.xpath(xpath)
    if element:
        text = element[0].text
        data.append([title, xpath, text])

# Save the data as CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'XPath', 'Text'])
    writer.writerows(data)