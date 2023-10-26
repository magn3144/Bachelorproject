import csv
from lxml import html

# Load HTML file
with open('downloaded_pages/amazon.html') as file:
    html_content = file.read()

# Parse HTML
tree = html.fromstring(html_content)

# Extract recently viewed items and featured recommendations
recently_viewed_items = tree.xpath('/html/body/div[1]/div[2]/div/noscript/div/div[1]')[0].text.strip()
featured_recommendations = tree.xpath('/html/body/div[1]/div[2]/div/noscript/div/div[2]/div/div/div[1]')[0].text.strip()

# Save data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Recently Viewed Items', 'Featured Recommendations'])
    writer.writerow([recently_viewed_items, featured_recommendations])