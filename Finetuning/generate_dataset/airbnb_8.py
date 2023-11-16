import csv
from bs4 import BeautifulSoup

def extract_info(soup):
    data = []
    listings = soup.select('div._r243u8q.l1ovpqvx.dir.dir-ltr')
    for listing in listings:
        location = listing.select_one('div.t1jojoys.dir.dir-ltr').text
        stars_container = listing.select_one('div.t1qa5xaj.dir.dir-ltr')
        if stars_container and "Guest favorite" in stars_container.text:
            stars = 5
        else:
            stars = 0
        data.append([location, stars])
    return data

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Location", "Stars"])
        writer.writerows(data)

def main():
    with open("downloaded_pages/airbnb.html") as file:
        soup = BeautifulSoup(file, "lxml")
    data = extract_info(soup)
    save_to_csv(data)

if __name__ == "__main__":
    main()