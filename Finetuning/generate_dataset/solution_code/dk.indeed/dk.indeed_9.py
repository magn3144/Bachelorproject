import csv
from lxml import etree

# Load the HTML file
html_path = "downloaded_pages/dk.indeed.html"
with open(html_path, "r") as file:
    html_content = file.read()

# Parse the HTML content
tree = etree.HTML(html_content)

# Define the XPath expressions for the elements
xpaths = {
    "job_titles": [
        "/html/body/main/div/div[1]/div/div[5]/div[1]/div[5]/div/ul/li/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/a/span",
        "/html/body/main/div/div[1]/div/div[5]/div[1]/div[5]/div/ul/li[2]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[1]/h2/a/span",
        "/html/body/main/div/div[1]/div/div[5]/div[1]/div[5]/div/ul/li[11]/div/div[1]/div/div[1]/div/table[2]/tbody/tr[2]/td/div[2]/div/div/ul/li[1]/span/a[3]"],
    "job_descriptions": ["/html/body/main/div/div[1]/div/div[5]/div[1]/div[5]/div/ul/li/div/div[1]/div/div[1]/div/table[2]/tbody/tr[2]/td/div[1]/div",
                         "/html/body/main/div/div[1]/div/div[5]/div[1]/div[5]/div/ul/li[1]/div/div[1]/div/div[1]/div/table[2]/tbody/tr[2]/td/div[1]/div",
                         "/html/body/main/div/div[1]/div/div[5]/div[1]/div[5]/div/ul/li[5]/div/div[1]/div/div[1]/div/table[2]/tbody/tr[2]/td/div[1]/div"],
    "company_names": ["/html/body/main/div/div[1]/div/div[5]/div[1]/div[5]/div/ul/li/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[2]/div/span",
                      "/html/body/main/div/div[1]/div/div[5]/div[1]/div[5]/div/ul/li[7]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[2]/div/span"],
    "locations": ["/html/body/main/div/div[1]/div/div[5]/div[1]/div[5]/div/ul/li/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[2]/div/div",
                  "/html/body/main/div/div[1]/div/div[5]/div[1]/div[5]/div/ul/li[8]/div/div[1]/div/div[1]/div/table[1]/tbody/tr/td/div[2]/div/div"],
}

# Scrape the data using the XPath expressions
scraped_data = []
for xpath in xpaths["job_titles"]:
    job_title = tree.xpath(xpath)
    scraped_data.append({
        "Job Title": job_title[0].text if job_title else "",
    })

for xpath in xpaths["job_descriptions"]:
    job_description = tree.xpath(xpath)
    scraped_data.append({
        "Job Description": job_description[0].text if job_description else "",
    })

for xpath in xpaths["company_names"]:
    company_name = tree.xpath(xpath)
    scraped_data.append({
        "Company Name": company_name[0].text if company_name else "",
    })

for xpath in xpaths["locations"]:
    location = tree.xpath(xpath)
    scraped_data.append({
        "Location": location[0].text if location else "",
    })

# Save the scraped data as a CSV file
output_file = "scraped_data.csv"
fieldnames = scraped_data[0].keys()
with open(output_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(scraped_data)

print("Scraping completed! Data saved as scraped_data.csv.")