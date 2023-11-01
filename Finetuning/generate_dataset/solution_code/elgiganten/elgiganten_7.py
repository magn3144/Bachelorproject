import csv
from bs4 import BeautifulSoup

# Set the local path to the HTML file
html_file_path = "downloaded_pages/elgiganten.html"

# Set the target element XPath
target_element_xpath = "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/div[2]/elk-component-loader-wrapper/elk-cms-template-component-list/div/elk-cms-shell[4]/elk-content-carousel/div/elk-carousel/div/swiper/div/div[3]/elk-content-carousel-element/a/h3"

# Open the HTML file and create a BeautifulSoup object
with open(html_file_path, 'r') as file:
    html_data = file.read()
    soup = BeautifulSoup(html_data, 'html.parser')

# Find the target element using the given XPath
target_element = soup.select_one(target_element_xpath)

# Extract the text from the target element
if target_element:
    scraped_text = target_element.get_text(strip=True)
else:
    scraped_text = ""

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([scraped_text])