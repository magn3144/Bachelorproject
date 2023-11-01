import csv
from lxml import etree

# Define the HTML file path
html_file = "downloaded_pages/ældresagen.html"

# Define the XPaths for the hidden information and shortcuts in the footer
hidden_info_xpath = "/html/body/div[2]/footer/section/div/div[1]/div[2]/div/div/div"
shortcuts_xpath = "/html/body/div[2]/footer/section/div/div[1]/div[3]/ul"

# Create an empty list to store the scraped data
scraped_data = []

# Open the HTML file and parse it using lxml
with open(html_file, "r", encoding="utf-8") as file:
    html = file.read()
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.fromstring(html, parser)

    # Scrape the hidden information and append it to the scraped data list
    hidden_info_element = tree.xpath(hidden_info_xpath)
    hidden_info = hidden_info_element[0].text.strip() if hidden_info_element else ""
    scraped_data.append(hidden_info)

    # Scrape the shortcuts and append them to the scraped data list
    shortcuts_elements = tree.xpath(shortcuts_xpath + "/li")
    shortcuts = [element.text.strip() for element in shortcuts_elements]
    scraped_data.extend(shortcuts)

# Save the scraped data as CSV
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(scraped_data)