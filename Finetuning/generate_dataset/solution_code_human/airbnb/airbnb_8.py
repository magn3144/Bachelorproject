import csv
from bs4 import BeautifulSoup

# Load the HTML data from local file.
with open('downloaded_pages/airbnb.html', 'r') as file:
    page_content = file.read().replace('\n', '')

soup = BeautifulSoup(page_content, 'html.parser')
location_divs = soup.find_all("div", {"class": "t1jojoys dir dir-ltr"})
divs_text = [div.text for div in location_divs]

# Amount of stars for each location
listing_divs = soup.find_all("div", {"class": "g1qv1ctd c1v0rf5q dir dir-ltr"})
star_texts = []
for div in listing_divs:
    stars = div.find_all("span", {"class": "r1dxllyb dir dir-ltr"})
    star_text = [star.text for star in stars]
    star_texts.append(star_text)

# Save the data to a CSV file in two seperate columns.
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for div, span in zip(divs_text, star_texts):
        writer.writerow([div, span])