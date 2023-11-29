import csv
from bs4 import BeautifulSoup

# Load the HTML data from local file.
with open('downloaded_pages/airbnb.html', 'r') as file:
    page_content = file.read().replace('\n', '')

soup = BeautifulSoup(page_content, 'html.parser')

listing_divs = soup.find_all("div", {"class": "c4mnd7m dir dir-ltr"})
guest_favorites = []
location_divs_text = []
for div in listing_divs:
    guest_favorite_div = div.find("div", {"class": "t1qa5xaj dir dir-ltr"})
    if guest_favorite_div:
        guest_favorite_text = 'yes'
    else:
        guest_favorite_text = 'no'
    guest_favorites.append(guest_favorite_text)
    location_div = div.find("div", {"class": "t1jojoys dir dir-ltr"})
    location_text = location_div.text
    location_divs_text.append(location_text)

# Save the data to a CSV file in two seperate columns.
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for div, span in zip(location_divs_text, guest_favorites):
        writer.writerow([div, span])