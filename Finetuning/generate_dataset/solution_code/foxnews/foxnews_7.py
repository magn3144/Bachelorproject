import csv
from bs4 import BeautifulSoup

# Function to check if a hyperlink contains specific keywords
def contains_keywords(link):
    keywords = ['sports', 'politics', 'lifestyle']
    for keyword in keywords:
        if keyword.lower() in link.lower():
            return True
    return False

# Read the HTML file
with open('downloaded_pages/foxnews.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all hyperlinks on the page
hyperlinks = soup.find_all('a')

# Filter the hyperlinks by category
filtered_links = [link['href'] for link in hyperlinks if contains_keywords(link['href'])]

# Save the filtered links to CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Hyperlink'])
    writer.writerows([[link] for link in filtered_links])