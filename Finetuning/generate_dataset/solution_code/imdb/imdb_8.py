import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/imdb.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = etree.HTML(html_content)

# Find the release year of "Judgment at Nuremberg"
release_year_element = tree.xpath('/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[136]/div[2]/div/div/div[2]/span[1]')[0]
release_year = release_year_element.text

# Save the release year as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Release Year'])
    writer.writerow([release_year])

print("Scraped data has been saved as 'scraped_data.csv'.")