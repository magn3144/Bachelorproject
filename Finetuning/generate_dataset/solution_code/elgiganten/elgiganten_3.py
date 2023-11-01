import csv
from lxml import etree

# defining the XPaths for the target elements
xpaths = {
    'antal_varer': '/html/body/header/div[5]/div/div[5]/label/span/span[1]'
}

# opening the HTML file and parsing it
with open('downloaded_pages/elgiganten.html', 'r', encoding='utf-8') as f:
    html = f.read()
tree = etree.HTML(html)

# extracting the text from the target elements using XPaths
antal_varer = tree.xpath(xpaths['antal_varer'])[0].text if tree.xpath(xpaths['antal_varer']) else ""

# saving the scraped data as a CSV file
data = [['Antal varer i indkøbskurven']]
data.append([antal_varer])

with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)