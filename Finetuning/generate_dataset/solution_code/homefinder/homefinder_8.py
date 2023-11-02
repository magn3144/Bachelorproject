from lxml import etree
import csv

# Define the XPaths for the elements
xpaths = [
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[30]/a/div[1]/div[2]/div[1]",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[4]/a/footer/div[2]",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[1]/a/footer/div[1]/div/span",
    "/html/body/div/div/div/header/nav/div/div[2]/div/ul[1]/li/button/span[2]",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[1]/div[3]/a[2]",
    "/html/body/div/div/div/header/nav/div/div[2]/div/ul[2]/li[2]/a",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[1]/div/div[1]/h1",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[2]/div/p[2]",
    "/html/body/div/div/div/section/div[1]/div[4]/div[2]/div[4]/div[1]/div[2]/p",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[1]/div[2]/label",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[1]/div[1]/label",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[2]/div/h2[2]",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[2]/div/h2[3]",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[6]/a/div[1]/div[2]/div[1]",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[13]/a/div[1]/div[1]/div",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[27]/a/footer/div[1]/div/span",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[20]/a/div[2]/div/div[1]/span",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[1]/div[3]/a[10]",
    "/html/body/div/div/div/footer/nav/a[3]",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[8]/div/form/div/div[1]/p[1]",
    "/html/body/div/div/div/section/div[1]/div[4]/div[2]/div[4]/div[3]/div[2]/p",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[1]/div[3]/label",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[2]/div/h2[4]",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[1]/a/footer/div[1]/div/div/div/div",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[12]/a/footer/div[2]",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[23]/a/footer/div[1]/div/span",
    "/html/body/div/div/div/section/div[1]/div[2]/div/div/div[1]/div/div[1]/ul/li[3]/a/span",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[1]/div[2]/a[6]",
    "/html/body/div/div/div/footer/nav/a[7]",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[24]/div/div/div[1]/div/p[1]",
    "/html/body/div/div/div/section/div[1]/div[4]/div[2]/div[4]/p",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[2]/div/h2[5]",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[13]/a/div[1]/div[2]/div[2]",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[27]/a/footer/div[2]",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[2]/div[14]/a/div[2]/div/div[1]/span",
    "/html/body/div/div/div/section/div[1]/div[4]/div[1]/div[4]/div[1]/div[2]/a[9]"
]

# Open the HTML file and create an ElementTree
with open('downloaded_pages/homefinder.html', 'r') as file:
    html_data = file.read()
tree = etree.HTML(html_data)

# Scrape the descriptions using XPaths
descriptions = []
for xpath in xpaths:
    element = tree.xpath(xpath)
    if len(element) > 0:
        descriptions.append(element[0].text)
    else:
        descriptions.append('')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Description'])
    for description in descriptions:
        writer.writerow([description])