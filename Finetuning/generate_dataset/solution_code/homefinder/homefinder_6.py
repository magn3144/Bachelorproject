from lxml import etree
import csv

# Define the XPaths for the article title
article_title_xpath = "/html/body/div/div/div/header/nav/div/div[2]/div/ul[2]/li[2]/a"

# Open the HTML file
with open("downloaded_pages/homefinder.html", "r") as html_file:
    # Parse the HTML content
    tree = etree.parse(html_file)

    # Find the article title element using the XPath
    article_title_element = tree.xpath(article_title_xpath)

    # Extract the text from the article title element
    article_title = article_title_element[0].text.strip()

    # Save the scraped data as CSV
    with open("scraped_data.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Article Title"])
        writer.writerow([article_title])