import csv
from lxml import html

def get_elements(tree, xpath):
    elements = tree.xpath(xpath)
    return [element.text_content().strip() for element in elements]

def scrape_amazon():
    category = "E-commerce"
    webpage = "amazon"
    local_path = "downloaded_pages/amazon.html"
    task = "Collect all recommended products with trusted sustainability certifications"
    csv_file = "scraped_data.csv"

    with open(local_path, "r") as f:
        content = f.read()

    tree = html.fromstring(content)

    elements = get_elements(tree, "/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[3]/div[2]/div/div[2]/span")
    
    data = []
    for element in elements:
        if "trusted sustainability certification" in element.lower():
            data.append(element)

    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Category", "Webpage", "Task", "Data"])
        writer.writerow([category, webpage, task])

        for item in data:
            writer.writerow(["", "", "", item])

scrape_amazon()