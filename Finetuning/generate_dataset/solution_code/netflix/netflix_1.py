import csv
from bs4 import BeautifulSoup

# Open the HTML file
with open('downloaded_pages/netflix.html', 'r') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all movie titles and their corresponding XPaths
movie_titles = []
xpaths = []

for element in soup.find_all("span", class_="nm-collections-title-name"):
    movie_titles.append(element.text)
    xpaths.append(element.parent.get('xpath'))
   
# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Movie Title', 'XPath'])
    writer.writerows(zip(movie_titles, xpaths))