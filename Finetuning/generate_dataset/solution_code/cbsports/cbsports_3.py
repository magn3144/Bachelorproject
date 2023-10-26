from bs4 import BeautifulSoup
import csv

def extract_anchor_text():
    with open("downloaded_pages/cbsports.html") as file:
        soup = BeautifulSoup(file, "html.parser")
        anchors = soup.find_all("a")
        
        data = []
        for anchor in anchors:
            text = anchor.text.strip()
            data.append([text])
        
        with open("scraped_data.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data)

extract_anchor_text()