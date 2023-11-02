from bs4 import BeautifulSoup
import csv

# Read the HTML file
with open('downloaded_pages/espn.html', 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find the more sports section
more_sports_section = soup.find('ul', class_='more-sports')

# Extract titles and links from more sports section
titles = []
links = []

for item in more_sports_section.find_all('li'):
    title = item.a.get_text(strip=True)
    link = item.a['href']
    titles.append(title)
    links.append(link)

# Save data to CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Link'])
    for title, link in zip(titles, links):
        writer.writerow([title, link])