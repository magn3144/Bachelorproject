import csv
from bs4 import BeautifulSoup

# Open the HTML file and read its contents
with open('downloaded_pages/census.html') as file:
    html = file.read()

# Create a BeautifulSoup object with the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Find all the elements with the text 'Survey Respondents'
surveys = soup.find_all(text='Survey Respondents')

# Open a CSV file for writing
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['Survey Respondents'])

    # Write the target data row
    for survey in surveys:
        writer.writerow([survey])
