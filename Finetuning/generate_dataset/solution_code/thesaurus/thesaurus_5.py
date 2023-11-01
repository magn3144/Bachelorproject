import csv
from bs4 import BeautifulSoup

# Load the HTML file
with open('downloaded_pages/thesaurus.html', 'r') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find the popular horror movies and their ratings
movies = soup.select('div.cszHPcPE')
data = []
for movie in movies:
    name = movie.select_one('h3').text.strip()
    rating = movie.select_one('span.kWMGVL').text.strip()
    data.append([name, rating])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Movie Name', 'Rating'])
    writer.writerows(data)