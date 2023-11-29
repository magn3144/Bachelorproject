
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/DTU_entrepreneurship.html', 'r') as f:
    page_content = f.read()

# Parse the HTML
tree = html.fromstring(page_content)

# Find the Education link
education_link = tree.xpath('//*[@id="footerJob"]/div/div[2]/ul/li[2]/a')

# Extract the text from the link
education_text = education_link[0].text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([education_text])
