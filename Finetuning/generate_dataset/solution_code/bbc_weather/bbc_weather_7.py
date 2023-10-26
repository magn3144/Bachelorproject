import csv
from lxml import html

# Define the local path to the HTML file
file_path = "downloaded_pages/bbc_weather.html"

# Read the HTML file
with open(file_path, "r") as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Find the recent searches header
recent_searches_header = tree.xpath("/html/body/div[8]/div/div[1]/div/div/div[2]/div/div/div/div[5]/div[3]/div[1]/div/div/p")[0].text

# Write the scraped data to a CSV file
with open("scraped_data.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([recent_searches_header])