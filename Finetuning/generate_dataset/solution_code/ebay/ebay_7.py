import csv
from lxml import etree

def get_html_element(xpath, html_tree):
    elements = html_tree.xpath(xpath)
    if elements:
        return elements[0].text.strip()
    return ""

def main():
    file_path = "downloaded_pages/ebay.html"
    category = "E-commerce"
    task = "Scrape the title 'Pre-loved is always in style!'"

    with open(file_path, "r") as file:
        html = file.read()

    html_tree = etree.HTML(html)

    xpath = "/html/body/div[4]/div[2]/section/div[1]/div[2]/h1"
    title = get_html_element(xpath, html_tree)

    with open("scraped_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Task", "Title"])
        writer.writerow([category, task, title])

if __name__ == "__main__":
    main()