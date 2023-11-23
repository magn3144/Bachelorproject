import requests
from bs4 import BeautifulSoup
import csv

html_path = "downloaded_pages/DTU_entrepreneurship.html"
with open(html_path, "r") as f:
    page_content = f.read()

soup = BeautifulSoup(page_content, 'html.parser')

# Find all with class mainButton
header_buttons = soup.find_all("a", class_="mainButton")

header_text = [button.text for button in header_buttons]

with open("scraped_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for header in header_text:
        writer.writerow([header])