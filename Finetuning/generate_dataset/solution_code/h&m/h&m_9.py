import csv
from selenium import webdriver

# Variables
url = "file:///path/to/downloaded_pages/h&m.html"
category = "Clothing Websites"
html_elements = [
    {
        "xpath": "/html/body/div/div[3]/main/div[2]/ul/li[10]/section/article/div[2]/div/p/span",
        "name": "Price"
    },
    {
        "xpath": "/html/body/div/div[3]/main/div[2]/ul/li[11]/section/article/div[2]/div/p[2]",
        "name": "Member Price"
    },
    # Add more html elements here if needed
]

# Initialize the browser
browser = webdriver.Chrome()

# Load the page
browser.get(url)

# Scrape the data
scraped_data = []
for element in html_elements:
    xpath = element["xpath"]
    name = element["name"]
    element_data = browser.find_element_by_xpath(xpath).text
    scraped_data.append({
        "Name": name,
        "Value": element_data
    })

# Close the browser
browser.quit()

# Save the data as CSV
with open("scraped_data.csv", "w", newline="") as csv_file:
    fieldnames = ["Name", "Value"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(scraped_data)