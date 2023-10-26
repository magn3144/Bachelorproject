import csv
from bs4 import BeautifulSoup

# Define the HTML file path
file_path = 'downloaded_pages/fifa.html'

# Define the target elements and their XPaths
elements = [
    {'text': 'Download the FIFA App today to enjoy more', 'xpath': '/html/body/div/div/div[2]/footer/div/section[1]/div/div[3]'},
    {'text': 'Host Country 2023: Indonesia', 'xpath': '/html/body/div/div/main/div/section[3]/div/div/div[1]/h2'},
    {'text': 'Manchester City star won Golden Ball award at 2017', 'xpath': '/html/body/div/div/main/div/section[1]/div/div[2]/div/div/div[1]/div[1]/a/div/div[2]/div/div/p'},
    {'text': 'Discover', 'xpath': '/html/body/div/div/main/div/section[1]/div/div[2]/div/div/div[1]/div[2]/a/div/div[2]/div/p'},
    {'text': 'Tyler Hall discusses training with Lionel Messi an', 'xpath': '/html/body/div/div/main/div/section[2]/div/div[2]/div[1]/div/a/div/div/div[2]/div/p'},
    {'text': 'Interview', 'xpath': '/html/body/div/div/main/div/section[1]/div/div[2]/div/div/div[1]/div[1]/a/div/div[2]/div/p'},
    {'text': 'Draw lays out path to glory, with past two champio', 'xpath': '/html/body/div/div/main/div/section[1]/div/div[2]/div/div/div[1]/div[2]/a/div/div[2]/div/div/p'},
    {'text': 'How every host nation fared at the U-17 World Cup', 'xpath': '/html/body/div/div/main/div/section[2]/div/div[2]/div[2]/div/div[4]/div/a/div/div/div[2]/div/div/div[1]/h4/span[1]/span'},
    {'text': 'Four previous winners have qualified to return to ', 'xpath': '/html/body/div/div/main/div/section[3]/div/div/div[1]/div/p[2]'},
]

# Scrape the website and extract the required information
def scrape_website(file_path, elements):
    # Load the HTML file
    with open(file_path, 'r') as file:
        html_content = file.read()

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the required information
    scraped_data = []
    for element in elements:
        text = soup.find('xpath', {'data-xpath': element['xpath']}).text
        scraped_data.append({'description': text})

    return scraped_data

# Save the scraped data as a CSV file
def save_to_csv(data):
    fieldnames = ['description']

    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Scrape the website and save the data to a CSV file
scraped_data = scrape_website(file_path, elements)
save_to_csv(scraped_data)