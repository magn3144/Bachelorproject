import csv
import lxml.html as lh

# Load the HTML file
file_path = 'downloaded_pages/amazon.html'
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
doc = lh.fromstring(html_content)

# Extract all customer reviews and ratings using XPath
reviews = doc.xpath('//div[@data-hook="review"]')
data = []
for review in reviews:
    rating = review.xpath('.//span[@class="a-icon-alt"]/text()')[0]
    text = review.xpath('.//span[@data-hook="review-body"]/text()')[0].strip()
    data.append([rating, text])

# Save the scraped data as CSV
output_path = 'scraped_data.csv'
with open(output_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Rating', 'Review'])
    writer.writerows(data)