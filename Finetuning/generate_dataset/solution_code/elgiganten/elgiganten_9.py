import csv
import requests
from lxml import html

# Define the target page URL
url = "https://www.elgiganten.dk/"

# Load the HTML content
response = requests.get(url)
tree = html.fromstring(response.content)

# Extract the text from the "©2023 Elgiganten A/S | Arne Jacobsens Allé 16, 2." p
text = tree.xpath('/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/elk-component-loader-wrapper/elk-footer/footer/div[2]/elk-footer-logo/div/div[2]/p[1]/text()')[0]

# Write the scraped data to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Text'])
    writer.writerow([text])