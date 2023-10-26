import csv
from lxml import etree

# Define the XPath expressions for the salary information
salary_xpath = [
    "/html/body/main/div/div[1]/div/div[5]/div[1]/div[5]/div/ul/li/div/div[1]/div/div[1]/div/table[2]/tbody/tr[2]/td/div[2]/div/div/ul/li/span/a",
    "/html/body/main/div/div[1]/div/div[5]/div[1]/div[5]/div/ul/li/div/div[1]/div/div[1]/div/table[2]/tbody/tr[2]/td/div[2]/div/div/ul/li/span/a[2]",
    "/html/body/main/div/div[1]/div/div[5]/div[1]/div[5]/div/ul/li/div/div[1]/div/div[1]/div/table[2]/tbody/tr[2]/td/div[2]/div/div/ul/li[2]/span/a",
    "/html/body/main/div/div[1]/div/div[5]/div[1]/div[5]/div/ul/li/div/div[1]/div/div[1]/div/table[2]/tbody/tr[2]/td/div[2]/div/div/ul/li[2]/span/a[3]"
]

# Open the local HTML file
with open("downloaded_pages/dk.indeed.html", "rb") as f:
    # Parse the HTML document
    tree = etree.parse(f)

    # Initialize the list to store the extracted salary information
    salaries = []

    # Extract the salary information using the XPath expressions
    for xpath in salary_xpath:
        salary_elements = tree.xpath(xpath)
        for elem in salary_elements:
            salaries.append(elem.text)

    # Save the extracted salary information into a CSV file
    with open("scraped_data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Salary"])
        writer.writerows([[salary] for salary in salaries])