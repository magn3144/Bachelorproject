import csv
from lxml import html

# Define the XPaths for the required information
title_xpath = "/html/head/title"
price_xpath = "/html/body/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr/td[9]/a/span"
change_xpath = "/html/body/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr/td[10]/a/span"
sector_xpath = "/html/body/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr/th[4]"
industry_xpath = "/html/body/div[3]/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/tr/th[5]"

# Open the HTML file and parse it using lxml
with open('downloaded_pages/finviz.html', 'r') as file:
    content = file.read()
tree = html.fromstring(content)

# Extract the required information using the XPaths
title = tree.xpath(title_xpath)[0].text.strip()
prices = tree.xpath(price_xpath)
changes = tree.xpath(change_xpath)
sectors = tree.xpath(sector_xpath)
industries = tree.xpath(industry_xpath)

# Create a list of dictionaries to store the scraped data
data = []
for i in range(len(prices)):
    data.append({
        'Title': title,
        'Price': prices[i].text.strip(),
        'Change': changes[i].text.strip(),
        'Sector': sectors[i].text.strip(),
        'Industry': industries[i].text.strip()
    })

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Title', 'Price', 'Change', 'Sector', 'Industry'])
    writer.writeheader()
    writer.writerows(data)