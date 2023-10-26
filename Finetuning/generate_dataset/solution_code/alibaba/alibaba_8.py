from bs4 import BeautifulSoup
import csv

# Open the HTML file
with open('downloaded_pages/alibaba.html', 'r') as f:
    html = f.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all p elements with class cerf-children-after__desc
p_elements = soup.find_all('p', {'class': 'cerf-children-after__desc'})

# Extract the text from p elements
texts = [p.get_text() for p in p_elements]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Scraped Text'])
    writer.writerows([[text] for text in texts])