import csv
from bs4 import BeautifulSoup

def write_to_csv(buttons):
    with open("scraped_data.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Button Text"])
        for button in buttons:
            writer.writerow([button])

def get_button_texts(path):
    with open(path, "r") as file:
        soup = BeautifulSoup(file, "html.parser")
        nav = soup.find('nav')
        if nav is not None:
            anchors = nav.find_all('a')
            return [anchor.text for anchor in anchors]
        return []

path = "downloaded_pages/DTU_entrepreneurship.html"
buttons = get_button_texts(path)
write_to_csv(buttons)