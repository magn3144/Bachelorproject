import csv
from bs4 import BeautifulSoup

html_file = "downloaded_pages/washingtonpost.html"

with open(html_file, "r") as f:
    soup = BeautifulSoup(f, "html.parser")

span_tags = soup.find_all("span", class_="Politics")

data = []
for tag in span_tags:
    data.append(tag.text)

with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for item in data:
        writer.writerow([item])