import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/seekingalpha.html', 'r') as file:
    html_content = file.read()

# Create an XPath parser
parser = html.fromstring(html_content)

# Find the first 100 articles
articles = parser.xpath('/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[2]/section/div/div/div/div[2]/article[position() <= 100]')

# Extract the body text of each article
data = []
for article in articles:
    body_text = article.xpath('.//div[@class="g_q r_d0"]/text()')[0]
    data.append(body_text)

# Save the scraped data in a CSV file
with open('scraped_data.csv','w',newline='') as file:
    writer = csv.writer(file)
    for item in data:
        writer.writerow([item])