import csv
from lxml import etree

# Define the XPath expressions for the subtitles
subtitles_xpath = [
    '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[6]/div/div/div[4]/a/div/div[2]/div',
    '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[2]/div/div/div[4]/a/div/div[2]/div',
    '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[6]/div/div/div[2]/a/div/div[2]/div',
    '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[2]/div/div/div[1]/a/div/div[2]/div',
    '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[6]/div/div/div[3]/a/div/div[2]/div',
    '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[2]/div/div/div[2]/a/div/div[2]/div',
    '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[5]/div/div[2]/div/div[1]/article/div[1]/p',
    '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[4]/div/div/div[1]/p',
    '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[3]/div/div/div[2]/div/div[4]/a/span[1]/span',
    '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[3]/div/div/div[2]/div/div[6]/a/span[1]/span',
    '/html/body/div[1]/div/div[3]/div[2]/main/div/div/div[5]/div/div[1]/p'
]

# Initialize the list to store the scraped subtitles
scraped_data = []

# Parse the HTML file
with open('downloaded_pages/jysk.html', 'r') as f:
    html = f.read()
    tree = etree.HTML(html)

    # Scrape the subtitles
    for xpath in subtitles_xpath:
        elements = tree.xpath(xpath)
        for element in elements:
            scraped_data.append(element.text.strip())

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Subtitles"])
    writer.writerows(zip(scraped_data))