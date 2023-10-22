import csv
from bs4 import BeautifulSoup

# Define the list of HTML elements containing the target data
html_elements = [
    '<a class="uscb-pagination-item">6</a>',
    '<p class="uscb-sub-heading-2 uscb-color-primary uscb-margin-TB-5">  of  17</p>',
    '<a class="uscb-pagination-item">8</a>',
    '<a class="uscb-pagination-item">10</a>',
    '<a class="uscb-pagination-item">2</a>',
    '<a class="uscb-pagination-item">7</a>'
]

# Extract the number of pages from the HTML elements
pages_list = [int(BeautifulSoup(element, 'html.parser').text.strip()) for element in html_elements]

# Calculate the total number of pages
total_pages = sum(pages_list)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Number of Pages'])
    writer.writerow([total_pages])