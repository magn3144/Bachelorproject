import csv
from lxml import html

# Define the XPaths for the release years
release_year_xpath = "/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li/div[2]/div/div/div[2]/span[1]"

# Parse the HTML file
with open('downloaded_pages/imdb.html', 'r') as file:
    content = file.read()
tree = html.fromstring(content)

# Extract the release years using XPath
release_years = [year.text.strip() for year in tree.xpath(release_year_xpath)]

# Save the release years as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Release Year'])
    writer.writerows(zip(release_years))