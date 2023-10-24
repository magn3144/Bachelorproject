import csv
from lxml import html

# Open the HTML file and parse it
with open('downloaded_pages/ppubs.html', 'r') as f:
    page_content = f.read()
tree = html.fromstring(page_content)

# Get the list of all patents
patent_elements = tree.xpath('//div[contains(@class, "card-patent")]')

# Extract data about all patents
data = []
for patent in patent_elements:
    patent_name = patent.xpath('.//h4[@class="card-title"]/text()')[0].strip()
    patent_number = patent.xpath('.//td[1]/text()')[0].strip()
    inventor_name = patent.xpath('.//td[5]/text()')[0].strip()
    data.append([patent_name, patent_number, inventor_name])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Patent Name', 'Patent Number', 'Inventor Name'])
    writer.writerows(data)