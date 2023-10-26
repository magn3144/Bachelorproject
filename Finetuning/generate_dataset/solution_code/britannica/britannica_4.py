import csv
from bs4 import BeautifulSoup

# Open the HTML file
with open('downloaded_pages/britannica.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')

# Find all the links containing questions about the human body
question_links = soup.find_all('a', string='How', class_='font-weight-semi-bold d-block mb-5 font-16')

# Extract the text from the question links
question_texts = [link.text.strip() for link in question_links]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Question'])
    writer.writerows([[question] for question in question_texts])