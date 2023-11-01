import csv
from lxml import etree

# Define the target page and local path to the HTML file
target_page = 'elgiganten'
html_file = 'downloaded_pages/elgiganten.html'

# Define the XPath for the "Gaming" span
gaming_xpath = '/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/div[2]/elk-component-loader-wrapper/elk-cms-template-component-list/div/elk-cms-shell[1]/elk-category-carousel/elk-image-slider/elk-carousel/div/swiper/div/div[6]/elk-image-title-element/a/span'

# Parse the HTML file
tree = etree.parse(html_file)

# Find the "Gaming" span element
gaming_span = tree.xpath(gaming_xpath)

# Extract the text from the "Gaming" span
gaming_text = gaming_span[0].text if gaming_span else ''

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Category', 'Element Text'])
    writer.writerow([target_page, gaming_text])