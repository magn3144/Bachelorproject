import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/trustpilot.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Get the list of recently reviewed companies
company_elements = tree.xpath("//div[contains(@class, 'styles_review')]")

# Extract company names and ratings
data = []
for company_element in company_elements:
    name = company_element.xpath(".//a[@class='link_internal__7XN06 typography_body-m__xgxZ_ typography_appearance-default__AAY17 link_link__IZzHN link_notUnderlined__szqki']/text()")[0]
    rating = company_element.xpath(".//p[contains(@class, 'styles_reviewBody')]/text()")[0]
    data.append([name, rating])

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Company', 'Rating'])
    writer.writerows(data)