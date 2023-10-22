import csv
from bs4 import BeautifulSoup

# target HTML file path
html_file = 'downloaded_pages/merchantcircle.html'

# target category
category = 'Directories'

# target HTML elements
elements = [
    '<a class="itemDesc">Save money? Call 347-263-7630</a>',
    '<a class="itemDesc">https://www.movers-newyorkcity.com</a>',
    '<a class="itemDesc">FOR A FREE MOVING ESTIMATE CONTACT US TODAY AT (34</a>',
    '<a class="itemDesc">pregabalin On Sale Cheap Online </a>'
]

# scrape the text from the itemDesc links
text_list = []
for element in elements:
    soup = BeautifulSoup(element, 'html.parser')
    text = soup.get_text()
    text_list.append(text)

# save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([category])
    writer.writerow(['Item Desc'])
    for text in text_list:
        writer.writerow([text])