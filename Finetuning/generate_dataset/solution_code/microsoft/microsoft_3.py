import csv
from lxml import html

# Define the web page category and local path to the HTML file
category = 'Forums and Review Sites'
path = 'downloaded_pages/microsoft.html'

# Define the XPath expressions for the desired elements
xpaths = {
    'option_1': '/html/body/div/div[4]/div/div/div/footer/div/a[2]/span',
    'option_2': '/html/body/div/div[4]/div/div/div/footer/div/noscript/a/span',
    'option_3': '/html/body/div/div[4]/div/div/div/footer/div/nav/ul/li[3]/a',
}

# Extract the text from the HTML using XPath
tree = html.parse(path)
data = {key: tree.xpath(xpath)[0].text for key, xpath in xpaths.items()}

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'Option'])
    writer.writerow([category, data['option_1']])
    writer.writerow([category, data['option_2']])
    writer.writerow([category, data['option_3']])