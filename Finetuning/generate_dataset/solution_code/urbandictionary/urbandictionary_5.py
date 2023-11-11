import csv
from lxml import etree

# Define the XPath for the Discord link
discord_xpath = "/html/body/div/header/div[2]/div[1]/div/div/ul/li[4]/a"

# Parse the HTML file
html_file = "downloaded_pages/urbandictionary.html"
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Find the Discord link using the XPath
discord_link = tree.xpath(discord_xpath)[0].text

# Save the scraped data as a CSV file
data = [['Link', 'XPath'],
        [discord_link, discord_xpath]]

with open('scraped_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)