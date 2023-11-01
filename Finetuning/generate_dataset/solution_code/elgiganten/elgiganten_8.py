import csv
from lxml import etree

# Define the target file path
file_path = "downloaded_pages/elgiganten.html"

# Define the Xpath for the "Månedens gaming gear" h3 element
xpath = "/html/body/div[1]/elk-app/ng-component/elk-base-template/mat-sidenav-container/mat-sidenav-content/div[2]/ng-component/div[2]/elk-component-loader-wrapper/elk-cms-template-component-list/div/elk-cms-shell[4]/elk-content-carousel/div/elk-carousel/div/swiper/div/div[1]/elk-content-carousel-element/a/h3"

# Parse the HTML file
with open(file_path, "r", encoding="utf-8") as file:
    html = file.read()
tree = etree.HTML(html)

# Scrape the text from the "Månedens gaming gear" h3 element
elements = tree.xpath(xpath)
scraped_data = [element.text for element in elements]

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Scraped Text"])
    writer.writerows(zip(scraped_data))