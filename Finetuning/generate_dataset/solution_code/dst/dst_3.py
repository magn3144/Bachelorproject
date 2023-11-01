import csv
from lxml import html

# Define the HTML file path
html_file = "downloaded_pages/dst.html"

# Define the XPaths for the target elements
contact_xpath = "/html/body/div[1]/main/div/div[2]/div[1]/div/div/div[6]/div/div[2]/div[2]"

# Parse the HTML file
with open(html_file, "r") as file:
    page_content = file.read()
tree = html.fromstring(page_content)

# Extract the contact information
contact_element = tree.xpath(contact_xpath)[0]
contact_info = contact_element.text.strip()

# Save the contact information to a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Contact Information"])
    writer.writerow([contact_info])