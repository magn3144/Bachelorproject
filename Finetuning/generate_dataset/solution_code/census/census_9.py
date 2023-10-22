import csv
from bs4 import BeautifulSoup

# Open the HTML file
with open('downloaded_pages/census.html') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all tags labeled as "Dataset"
dataset_tags = soup.find_all('span', class_='uscb-tag-label')

# Extract the text from the dataset tags
dataset_list = [tag.text for tag in dataset_tags]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Scraped Data'])
    writer.writerows(zip(dataset_list))