import csv
from bs4 import BeautifulSoup

# load the HTML file
html_file = open('downloaded_pages/h&m.html', 'r')
html_content = html_file.read()
html_file.close()

# parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# find the title tag with id "hmdefault-logo"
title_element = soup.find('title', id='hmdefault-logo')

# get the text content of the title tag
title_text = ""
if title_element:
    title_text = title_element.get_text()

# save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([title_text])