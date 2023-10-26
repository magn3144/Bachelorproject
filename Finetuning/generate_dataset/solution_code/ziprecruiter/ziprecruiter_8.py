import csv
from lxml import etree

def extract_label_data(tree, xpath):
    elements = tree.xpath(xpath)
    return [element.text for element in elements if element.text]

def scrape_data():
    html_file = "downloaded_pages/ziprecruiter.html"
    xpath_mapping = {
        "First Name": "/html/body/main/div/div/div/div/div[1]/div/div[2]/div/div[2]/form/div[2]/label",
        "Last Name": "/html/body/main/div/div/div/div/div[1]/div/div[2]/div/div[2]/form/div[3]/label",
        "Email": "/html/body/main/div/div/div/div/div[1]/div/div[2]/div/div[2]/form/div[4]/label",
        "Phone": "/html/body/main/div/div/div/div/div[1]/div/div[2]/div/div[2]/form/div[5]/label",
        "Resume": "/html/body/main/div/div/div/div/div[1]/div/div[2]/div/div[2]/form/div[7]/label",
    }

    with open(html_file, "rb") as file:
        tree = etree.parse(file)

        data = {}
        for label, xpath in xpath_mapping.items():
            data[label] = extract_label_data(tree, xpath)

    with open("scraped_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data.keys())
        writer.writerows(zip(*data.values()))

if __name__ == "__main__":
    scrape_data()