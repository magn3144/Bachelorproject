import csv
from lxml import etree

# Define the target elements and their corresponding XPaths
elements = [
    {"element": "span", "xpath": "/html/body/div[1]/div[1]/a/span[1]"},
    {"element": "span", "xpath": "/html/body/div[1]/nav/div[1]/ul/li[5]/div/ul/li[5]/a/span"},
    {"element": "div", "xpath": "/html/body/div[1]/nav/ul/ul[2]/li[3]/button/span/div[1]"},
    {"element": "h3", "xpath": "/html/body/div[1]/div[3]/div/div/div[1]/div[2]/h3"},
    {"element": "label", "xpath": "/html/body/div[1]/div[3]/div/div/div[1]/form/div[2]/div/div[1]/label"},
    {"element": "a", "xpath": "/html/body/div[1]/div[4]/div/div/div[2]/a"},
    {"element": "p", "xpath": "/html/body/div[1]/div[4]/div/div/div[1]/p"},
    {"element": "span", "xpath": "/html/body/div[1]/nav/div[1]/ul/li[6]/div/ul/li[3]/button/span[2]"},
    {"element": "div", "xpath": "/html/body/div[1]/nav/div[1]/ul/li[6]/button/span/div[1]"},
    {"element": "label", "xpath": "/html/body/div[1]/div[3]/div/div/div[1]/form/div[1]/label"},
    {"element": "a", "xpath": "/html/body/div[1]/div[3]/div/div/div[2]/a"},
    {"element": "span", "xpath": "/html/body/div[1]/nav/ul/ul[1]/li[3]/div/ul/li[2]/a/span"},
    {"element": "a", "xpath": "/html/body/div[1]/div[3]/div/div/div[1]/form/div[2]/div/div[2]/a"},
    {"element": "span", "xpath": "/html/body/div[1]/nav/div[1]/ul/li[3]/div/ul/li[1]/a/span[1]"}
]

# Load the HTML file
html_path = "downloaded_pages/artstation.html"
with open(html_path, "r") as file:
    html_content = file.read()

# Parse the HTML content
html = etree.HTML(html_content)

# Extract the newsletter titles
newsletter_titles = []
for element in elements:
    if element["element"] == "span" or element["element"] == "a":
        elements_list = html.xpath(element["xpath"])
        for el in elements_list:
            newsletter_titles.append(el.text.strip())

# Save the scraped data as a CSV file
csv_path = "scraped_data.csv"
with open(csv_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Newsletter Title"])
    writer.writerows([[title] for title in newsletter_titles])