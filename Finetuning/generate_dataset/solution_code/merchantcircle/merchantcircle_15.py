import csv
from bs4 import BeautifulSoup

html_file = "downloaded_pages/merchantcircle.html"

with open(html_file) as f:
    soup = BeautifulSoup(f, "html.parser")

btnDir_links = soup.find_all("a", class_="btnDir")

data = []
for link in btnDir_links:
    data.append(link.get_text())

with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(zip(data))