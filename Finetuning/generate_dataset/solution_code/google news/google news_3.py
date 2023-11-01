import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/google news.html', 'r') as file:
    html_data = file.read()

# Create a soup object
soup = BeautifulSoup(html_data, 'html.parser')

# Find all div tags with class "EY8ABd-OWXEXe-TAWMXe" and id "tt-i23"
div_tags = soup.find_all('div', class_='EY8ABd-OWXEXe-TAWMXe', id='tt-i23')

# Extract the text and corresponding XPaths
data = []
for div_tag in div_tags:
    text = div_tag.text.strip()
    xpath = soup.find(string=text).parent.xpath('ancestor-or-self::node()/div')
    data.append([text, xpath])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Text', 'XPath'])
    writer.writerows(data)