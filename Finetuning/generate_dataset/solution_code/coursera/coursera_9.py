import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/coursera.html', 'r') as file:
    html = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all hidden pages
hidden_pages = soup.find_all('title', text='Hidden pages')

# Extract the URLs of hidden pages
urls = []
for page in hidden_pages:
    url = page.find_parent('li').find('a')['href']
    urls.append(url)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['URL'])
    writer.writerows(zip(urls))