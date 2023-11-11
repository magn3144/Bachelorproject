import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/urbandictionary.html', 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find the Facebook link
facebook_element = soup.find('span', text='Facebook')
if facebook_element:
    facebook_link = facebook_element.parent['href']
    facebook_xpath = facebook_element.parent.xpath('ancestor::a')[0].xpath('string(.)')
else:
    facebook_link = ''
    facebook_xpath = ''

# Save scraped data as CSV
data = [['Category', 'Link', 'XPath'], ['Educational Websites', facebook_link, facebook_xpath]]

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)