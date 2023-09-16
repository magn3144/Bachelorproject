import csv
import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://monstercat.fandom.com/wiki/Silk_Music_Discography"
response = requests.get(url)
response.raise_for_status()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all tables in the page
tables = soup.find_all("table")

# Initialize lists to store LP names and artists
lp_names = []
lp_artists = []

# Process each table in the page
for table in tables:
    # Check if the table has more than 3 columns
    if len(table.find_all("td")) > 3:
        # Find all rows in the table
        rows = table.find_all("tr")
        
        # Process each row in the table
        for row in rows[1:]:
            # Find the LP name and artist elements in the row
            name_elem = row.find_all("td")[1]
            artist_elem = row.find_all("td")[2]
            
            # Extract the text from the elements
            lp_name = name_elem.get_text(strip=True)
            lp_artist = artist_elem.get_text(strip=True)
            
            # Add the LP name and artist to the respective lists
            lp_names.append(lp_name)
            lp_artists.append(lp_artist)

# Write the LP names and artists to a CSV file
csv_file = "lp_data.csv"
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Name", "Artist"])  # Write header row
    writer.writerows(zip(lp_names, lp_artists))

print("Data saved to", csv_file)