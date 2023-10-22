from bs4 import BeautifulSoup
import csv

# Load the HTML file
with open('downloaded_pages/espn.html') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all legal footer links
footer_links = soup.find_all('a', class_='AnchorLink LegalFooter__Link LegalFooter__Link--underline-hover')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Link'])

    for link in footer_links:
        writer.writerow([link['href']])