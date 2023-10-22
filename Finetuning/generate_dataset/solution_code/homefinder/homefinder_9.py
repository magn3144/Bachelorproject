import csv
from bs4 import BeautifulSoup

html_file = "downloaded_pages/homefinder.html"
target_elements = [
    "<span class='scope-label text-homes-for-sale small'>",
    "<span class='scope-label text-homes-for-sale small'>",
    "<span class='scope-label text-homes-for-sale small'>",
]

property_types = []

with open(html_file, "r") as file:
    soup = BeautifulSoup(file, "html.parser")
    for element in target_elements:
        tags = soup.find_all("span", class_="scope-label text-homes-for-sale small")
        for tag in tags:
            property_types.append(tag.text.strip())

with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Property Type"])
    for property_type in property_types:
        writer.writerow([property_type])