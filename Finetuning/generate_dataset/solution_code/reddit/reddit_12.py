import csv
from lxml import html

html_file = "downloaded_pages/reddit.html"
csv_file = "scraped_data.csv"

# Define the target XPaths for the links to other community discussions
link_xpaths = [
    "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[4]/a",
    "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[47]/div/div/div/div[2]/div[2]/div[2]/div/p[1]/a[1]",
    "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[205]/div/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/template/button/span[2]/span",
    "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[8]/div/div/div/div[2]/div[2]/div[1]/span[2]/div/span"
]

def extract_links(tree):
    links = []
    for xpath in link_xpaths:
        elements = tree.xpath(xpath)
        for element in elements:
            links.append(element.get("href"))
    return links

def save_to_csv(data, file):
    with open(file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Links to Other Community Discussions"])
        writer.writerows(data)

# Read the HTML file and create an HTML tree
with open(html_file, "r") as file:
    content = file.read()
tree = html.fromstring(content)

# Extract the links to other community discussions
links = extract_links(tree)

# Save the links to a CSV file
save_to_csv(links, csv_file)