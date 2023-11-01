import csv
from lxml import etree

# Define the XPaths for the elements we want to scrape
label_xpath = "/html/body/div/main/div/div[4]/div/div/div[2]/div[2]/div[6]/span[30]/div/div/div[2]/div/div[1]/div[2]/div[2]/span/a/span"
name_xpath = "/html/body/div/main/div/div[4]/div/div/div[2]/div[2]/div[6]/span[30]/div/div/div[2]/div/div[1]/div[2]/div[1]/span/a/span"
address_xpath = "/html/body/div/main/div/div[4]/div/div/div[2]/div[2]/div[6]/span[30]/div/div/div[2]/header/div/div[2]/div[2]/div[2]/div[2]"

# Load the HTML file
tree = etree.parse("downloaded_pages/tripadvisor.html")

# Scrape the data
label = tree.xpath(label_xpath)[0].text
name = tree.xpath(name_xpath)[0].text
address = tree.xpath(address_xpath)[0].text

# Create a list with the scraped data
data = [[label, name, address]]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Label', 'Name', 'Address'])
    writer.writerows(data)