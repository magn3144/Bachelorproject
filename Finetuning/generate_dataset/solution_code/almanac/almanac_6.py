import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Load the local HTML file
with open('downloaded_pages/almanac.html') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find the Almanac's Daily Updates section
daily_updates_section = soup.find('a', text='Get Almanac\'s Daily Updates').parent.parent

# Find all the items in the section
items = daily_updates_section.find_all('p', class_='prod-title')

# Create a list to store the scraped data
data = []
for item in items:
    # Extract the name and price of each item
    name = item.text
    price = item.find_next('p').text

    # Append the data to the list
    data.append([name, price])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Item Name', 'Price'])
    writer.writerows(data)