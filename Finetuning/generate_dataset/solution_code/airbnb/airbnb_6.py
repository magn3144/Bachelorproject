from bs4 import BeautifulSoup
import csv
import os

path = './downloaded_pages/airbnb.html'

with open(path, 'r') as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'lxml')

header_node = soup.find("h2", string="Inspiration for future getaways")
popular_node = header_node.find_next_sibling("div")
locations = popular_node.find_all("div", class_="t1jojoys dir dir-ltr")

data = []
for location in locations:
    link = location.find_parent("a")["href"]
    text = location.text
    data.append([text, link])

with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Location", "Link"])
    writer.writerows(data)