import csv
from bs4 import BeautifulSoup

html_file = open("downloaded_pages/airbnb.html")
soup = BeautifulSoup(html_file, 'html.parser')

button = soup.find("button", string="Show more")

class_list = button.get("class")

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for clas in class_list:
        writer.writerow([clas])