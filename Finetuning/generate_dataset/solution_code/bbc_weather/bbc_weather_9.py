import csv
from lxml import etree

# Load the HTML file
html_file = 'downloaded_pages/bbc_weather.html'
with open(html_file, 'r') as file:
    html = file.read()

# Parse the HTML
tree = etree.HTML(html)

# Extract the latest forecast for London heading
latest_forecast_element = tree.xpath('//h3[contains(text(),"Latest forecast for London")]/text()')[0]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Latest Forecast for London'])
    writer.writerow([latest_forecast_element])