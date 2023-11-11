import csv
import os
from lxml import etree

# Local path to the HTML file
file_path = "downloaded_pages/booking.html"

# XPaths for the room descriptions
room_xpath1 = "/html/body/div[5]/div/div[4]/div[1]/div[1]/div[4]/div[2]/div[2]/div/div/div[3]//h4"
room_xpath2 = "/html/body/div[5]/div/div[4]/div[1]/div[1]/div[4]/div[2]/div[2]/div/div/div[3]//div[@class='aee5343fdb def9bc142a']"

# Parse HTML
parser = etree.HTMLParser()
tree = etree.parse(file_path, parser)

# Find room descriptions
rooms1 = tree.xpath(room_xpath1)
rooms2 = tree.xpath(room_xpath2)

# Combine room descriptions
room_descriptions = []
for room in rooms1:
    room_descriptions.append(room.text.strip())
for room in rooms2:
    room_descriptions.append(room.text.strip())

# Save room descriptions as CSV file
output_file = 'scraped_data.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Room Descriptions"])
    writer.writerows([[description] for description in room_descriptions])

# Print success message
print(f"Scraping completed. Data saved as {output_file}")