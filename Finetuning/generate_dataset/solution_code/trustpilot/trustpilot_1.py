import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open('downloaded_pages/trustpilot.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all forum and review site names
forum_names = []
review_site_names = []

# Find forum names using XPath
forum_elements = soup.find_all('span', text='Erhvervsforsikringsselskab')
for element in forum_elements:
    forum_names.append(element.text)

# Find review site names using XPath
review_site_elements = soup.find_all('span', {'class': 'typography_body-s__aY15Q', 'text': 'Rejseforsikringsselskab'})
for element in review_site_elements:
    review_site_names.append(element.text)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Forum Names'])
    writer.writerows(forum_names)
    writer.writerow([])
    writer.writerow(['Review Site Names'])
    writer.writerows(review_site_names)

print('Scraping completed and data saved as scraped_data.csv')