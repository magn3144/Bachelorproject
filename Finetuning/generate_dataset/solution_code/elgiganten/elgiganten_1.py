import csv
from bs4 import BeautifulSoup

# Define the local path to the HTML file
html_file = 'downloaded_pages/elgiganten.html'

# Open the HTML file and create a BeautifulSoup object
with open(html_file, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find the hyperlink with the text "Elgigantens databeskyttelsespolitik"
link_element = soup.find('a', text='Elgigantens databeskyttelsespolitik')

# Extract the link and text from the hyperlink
link = link_element['href']
text = link_element.get_text(strip=True)

# Create a list to store the scraped data
scraped_data = [[link, text]]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(scraped_data)