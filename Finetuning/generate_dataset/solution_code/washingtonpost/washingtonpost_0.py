import csv
from bs4 import BeautifulSoup

# Open the HTML file and read its content
with open('downloaded_pages/washingtonpost.html') as file:
    html_content = file.read()

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the headlines and their corresponding authors
headlines = soup.find_all('span')
authors = soup.find_all('a')

# Store the extracted data in a list of dictionaries
data = []
for i in range(len(headlines)):
    headline = headlines[i].text.strip()
    author = authors[i].text.strip()
    data.append({'Headline': headline, 'Author': author})

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Headline', 'Author'])
    writer.writeheader()
    writer.writerows(data)