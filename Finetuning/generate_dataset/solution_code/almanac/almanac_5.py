import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/almanac.html', 'r') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Scrape and save the long-range weather forecast for the next 2 months
forecast_elements = tree.xpath('/html/body/div[1]/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[1]/p')
forecast = ''
for elem in forecast_elements:
    forecast += elem.text_content()
    
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Long-range Weather Forecast'])
    writer.writerow([forecast])