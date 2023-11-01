import csv
from lxml import etree

# Define the HTML file path
html_path = "downloaded_pages/danielilett.html"

# Define the list of HTML elements and their corresponding XPaths
html_elements = [
    {"element": "span", "xpath": "/html/body/div[2]/span"},
    {"element": "a", "xpath": "/html/body/div[3]/div/div/article/p[387]/a[3]"},
    {"element": "a", "xpath": "/html/body/nav/div/div[2]/ul/li[1]/a"},
    {"element": "h1", "xpath": "/html/body/div[3]/div/div/article/h1[4]"},
    {"element": "h1", "xpath": "/html/body/div[3]/div/div/article/h1[12]"},
    {"element": "div", "xpath": "/html/body/div[2]/a/div"},
    {"element": "p", "xpath": "/html/body/div[3]/div/div/article/p[97]"},
    {"element": "h2", "xpath": "/html/body/div[3]/div/div/article/h2[19]"},
    {"element": "h2", "xpath": "/html/body/div[3]/div/div/article/h2[2]"},
    {"element": "h3", "xpath": "/html/body/div[3]/div/div/article/h3[10]"},
    {"element": "h3", "xpath": "/html/body/div[3]/div/div/article/h3[70]"},
    {"element": "h4", "xpath": "/html/body/div[3]/div/div/article/h4[1]"},
    {"element": "span", "xpath": "/html/body/footer/div/div/div/ul/li[3]/a/span[2]"},
    {"element": "a", "xpath": "/html/body/div[3]/div/div/article/p[387]/a[2]"},
    {"element": "a", "xpath": "/html/body/nav/div/div[2]/ul/li[2]/a"},
    {"element": "h1", "xpath": "/html/body/header/div[2]/div/div/div/div/h1"},
    {"element": "h1", "xpath": "/html/body/div[3]/div/div/article/h1[7]"},
    {"element": "p", "xpath": "/html/body/div[3]/div/div/article/p[344]"},
    {"element": "h2", "xpath": "/html/body/div[3]/div/div/article/h2[34]"},
    {"element": "h2", "xpath": "/html/body/div[3]/div/div/article/h2[1]"},
    {"element": "h3", "xpath": "/html/body/div[3]/div/div/article/h3[48]"},
    {"element": "h3", "xpath": "/html/body/div[3]/div/div/article/h3[169]"},
    {"element": "h4", "xpath": "/html/body/div[3]/div/div/article/h4[2]"},
    {"element": "span", "xpath": "/html/body/footer/div/div/div/ul/li[2]/a/span[2]"},
    {"element": "a", "xpath": "/html/body/div[3]/div/div/article/p[3]/a"},
    {"element": "a", "xpath": "/html/body/footer/div/div/div/p[2]/a"},
    {"element": "h1", "xpath": "/html/body/header/div[1]/div/div/div/div/div/h1"},
    {"element": "h1", "xpath": "/html/body/div[3]/div/div/article/h1[14]"},
    {"element": "p", "xpath": "/html/body/div[3]/div/div/article/p[8]"},
    {"element": "h2", "xpath": "/html/body/div[3]/div/div/article/h2[20]"},
    {"element": "h2", "xpath": "/html/body/div[3]/div/div/article/h2[38]"},
    {"element": "h3", "xpath": "/html/body/div[3]/div/div/article/h3[28]"},
    {"element": "h3", "xpath": "/html/body/div[3]/div/div/article/h3[168]"},
    {"element": "span", "xpath": "/html/body/nav/div/div[1]/button/span[1]"},
    {"element": "a", "xpath": "/html/body/div[3]/div/div/ul/li[1]/a"},
    {"element": "a", "xpath": "/html/body/nav/div/div[2]/ul/li[2]/div/a"},
    {"element": "h1", "xpath": "/html/body/div[3]/div/div/article/h1[9]"},
    {"element": "p", "xpath": "/html/body/div[3]/div/div/article/p[223]"},
    {"element": "h2", "xpath": "/html/body/div[3]/div/div/article/h2[3]"},
    {"element": "h2", "xpath": "/html/body/div[3]/div/div/article/h2[21]"},
    {"element": "h3", "xpath": "/html/body/div[3]/div/div/article/h3[177]"},
    {"element": "h3", "xpath": "/html/body/div[3]/div/div/article/h3[185]"},
    {"element": "span", "xpath": "/html/body/header/div[2]/div/div/div/div/span"},
    {"element": "a", "xpath": "/html/body/div[3]/div/div/article/p[387]/a[4]"},
    {"element": "h1", "xpath": "/html/body/div[3]/div/div/article/h1[10]"},
    {"element": "p", "xpath": "/html/body/div[3]/div/div/article/p[200]"},
    {"element": "h2", "xpath": "/html/body/div[3]/div/div/article/h2[35]"},
    {"element": "h3", "xpath": "/html/body/div[3]/div/div/article/h3[5]"},
    {"element": "h3", "xpath": "/html/body/div[3]/div/div/article/h3[66]"},
    {"element": "span", "xpath": "/html/body/footer/div/div/div/ul/li[4]/a/span[2]"},
    {"element": "a", "xpath": "/html/body/nav/div/div[2]/ul/li[3]/div/a[1]"},
    {"element": "h1", "xpath": "/html/body/div[3]/div/div/article/h1[11]"},
    {"element": "p", "xpath": "/html/body/div[3]/div/div/article/p[372]"},
    {"element": "h2", "xpath": "/html/body/div[3]/div/div/article/h2[23]"},
    {"element": "h3", "xpath": "/html/body/div[3]/div/div/article/h3[24]"},
    {"element": "h3", "xpath": "/html/body/div[3]/div/div/article/h3[30]"},
    {"element": "span", "xpath": "/html/body/header/div[1]/div/div/div/div/div/span"},
    {"element": "a", "xpath": "/html/body/nav/div/div[2]/ul/li[3]/a"},
    {"element": "h1", "xpath": "/html/body/div[3]/div/div/article/h1[13]"},
    {"element": "p", "xpath": "/html/body/div[3]/div/div/article/p[130]"},
    {"element": "h2", "xpath": "/html/body/div[3]/div/div/article/h2[20]"},
]

# Define the output CSV file path
output_csv = "scraped_data.csv"

# Parse the HTML file
with open(html_path, "r") as file:
    html_data = file.read()
tree = etree.HTML(html_data)

# Create a list to store the scraped data
scraped_data = []

# Scrape the elements and their corresponding XPaths
for element_info in html_elements:
    elements = tree.xpath(element_info["xpath"])
    if elements:
        text = elements[0].text.strip() if elements[0].text else ""
        scraped_data.append({"Element": element_info["element"], "Text": text, "XPath": element_info["xpath"]})

# Save the scraped data as a CSV file
with open(output_csv, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Element", "Text", "XPath"])
    writer.writeheader()
    writer.writerows(scraped_data)