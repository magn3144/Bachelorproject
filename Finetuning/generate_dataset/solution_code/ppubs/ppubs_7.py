import csv
from bs4 import BeautifulSoup

# Open the HTML file and create a BeautifulSoup object
with open('downloaded_pages/ppubs.html', 'r') as file:
    html_data = file.read()
    soup = BeautifulSoup(html_data, 'html.parser')

# Find all the modal pop-ups on the webpage
modals = soup.find_all(class_='modal-dialog')

# Create a list to store the scraped data
scraped_data = []

# Loop through each modal pop-up
for modal in modals:
    # Find the title of the modal
    title = modal.find(class_='modal-title').text.strip()
    
    # Find the content of the modal
    content = modal.find(class_='modal-body').text.strip()
    
    # Append the scraped data to the list
    scraped_data.append([title, content])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(scraped_data)