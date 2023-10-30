import csv
from lxml import html

# Define the target page URL
url = 'file://localhost/downloaded_pages/woman.html'

# Define the XPaths for the links to series and quizzes
series_xpath = "//a[contains(.,'Serier')]"
quizzes_xpath = "//a[contains(.,'Quizzer')]"

# Create an empty list to store the scraped links
links = []

# Parse the HTML file
tree = html.parse(url)

# Find all the links to series and quizzes
series_links = tree.xpath(series_xpath)
quizzes_links = tree.xpath(quizzes_xpath)

# Add the series links to the list
for link in series_links:
    links.append(link.attrib['href'])

# Add the quizzes links to the list
for link in quizzes_links:
    links.append(link.attrib['href'])

# Write the scraped links to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(links)

print("Scraping complete. The data has been saved as scraped_data.csv")