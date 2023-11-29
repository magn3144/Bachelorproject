import csv
from bs4 import BeautifulSoup

# Load the HTML data from local file.
with open('downloaded_pages/airbnb.html', 'r') as file:
    page_content = file.read().replace('\n', '')

soup = BeautifulSoup(page_content, 'html.parser')
divs = soup.find_all("div", {"class": "t1jojoys dir dir-ltr"})
divs_text = [div.text for div in divs]

# Link elements for each location
# The parent element
location_divs = soup.find_all("div", {"class": "dir dir-ltr"})
# The first <a> child element
location_link_elems = [div.find('a') for div in location_divs][1:]
# The link for each location (checks if the link exists)
location_links = [link['href'] if link else None for link in location_link_elems]
# Remove empty strings from the list
location_links = list(filter(None, location_links))
# Remove dublicates
location_links = list(dict.fromkeys(location_links))

# Save the data to a CSV file in two seperate columns.
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for div, span in zip(divs_text, location_links):
        writer.writerow([div, span])