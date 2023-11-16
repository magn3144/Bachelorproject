from bs4 import BeautifulSoup
import csv

with open("downloaded_pages/airbnb.html", "r") as f:
    contents = f.read()

soup = BeautifulSoup(contents, 'lxml')

footer = soup.find_all('footer')

data = [["Support",[]], ["Hosting",[]], ["Airbnb",[]]]

for section in footer:
    headings = section.find_all('h3')
    for heading in headings:
        if heading.text == "Support":
            links = heading.find_next_sibling('ul').find_all('a')
            for link in links:
                data[0][1].append(link.text)
        elif heading.text == "Hosting":
            links = heading.find_next_sibling('ul').find_all('a')
            for link in links:
                data[1][1].append(link.text)
        elif heading.text == "Airbnb":
            links = heading.find_next_sibling('ul').find_all('a')
            for link in links:
                data[2][1].append(link.text)

with open('scraped_data.csv', 'w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)