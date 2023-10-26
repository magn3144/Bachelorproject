import csv
from lxml import etree

def scrape_violent_crimes():
    # Load the HTML file
    with open("downloaded_pages/fbi.html", "rb") as file:
        html = file.read()

    # Parse the HTML
    parser = etree.HTMLParser()
    tree = etree.fromstring(html, parser)

    # Find the violent crimes elements
    elements = tree.xpath('//a[contains(text(), "Violent Crimes")]')

    # Extract the names and links
    names = [element.text for element in elements]
    links = [element.get("href") for element in elements]

    # Save the scraped data as a CSV file
    with open("scraped_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Link"])
        for name, link in zip(names, links):
            writer.writerow([name, link])

scrape_violent_crimes()