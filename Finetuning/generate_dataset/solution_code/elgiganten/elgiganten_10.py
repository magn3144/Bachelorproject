from lxml import html
import csv

# Load the HTML file
html_file = "downloaded_pages/elgiganten.html"
with open(html_file, "r", encoding="utf-8") as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Define the XPath for the target element
element_xpath = '/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/div[2]/elk-component-loader-wrapper/elk-cms-template-component-list/div/elk-cms-shell[6]/elk-content-carousel/div[1]/h2'

# Scrape the text from the target element
target_element = tree.xpath(element_xpath)[0]
text = target_element.text.strip()

# Write the scraped data to a CSV file
csv_file = "scraped_data.csv"
with open(csv_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Text from 'Lad elektronikken køre i ring' h2"])
    writer.writerow([text])