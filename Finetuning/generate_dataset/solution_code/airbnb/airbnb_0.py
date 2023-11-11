import csv
from pathlib import Path
from bs4 import BeautifulSoup

# Open the HTML file
file_path = Path("downloaded_pages/airbnb.html")
with open(file_path, "r") as file:
    html_content = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, "html.parser")

# Find all the Airbnb-friendly apartments
apartments = soup.find_all("a", class_="l1ovpqvx c1kblhex dir dir-ltr")

# Store the apartments in a list
apartment_list = [apartment.text for apartment in apartments]

# Save the scraped data as a CSV file
csv_file = Path("scraped_data.csv")
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Apartment"])
    writer.writerows(apartment_list)