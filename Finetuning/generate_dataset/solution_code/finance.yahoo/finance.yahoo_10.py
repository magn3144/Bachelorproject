import csv
from lxml import etree

# Load the HTML file
html_path = "downloaded_pages/finance.yahoo.html"
with open(html_path, "r") as file:
    html_content = file.read()

# Parse the HTML content
parser = etree.HTMLParser()
tree = etree.parse(html_path, parser)

# Get the mail element
mail_element_xpath = "/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/ul/li[3]/a/span"
mail_element = tree.xpath(mail_element_xpath)[0].text

# Save the scraped data as CSV
csv_path = "scraped_data.csv"
with open(csv_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Mail"])
    writer.writerow([mail_element])

print("Scraped data has been saved as scraped_data.csv")