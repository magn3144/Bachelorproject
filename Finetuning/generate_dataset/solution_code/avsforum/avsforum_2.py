import csv
from lxml import html

# Parse the HTML file
with open('downloaded_pages/avsforum.html', 'r') as file:
    page_content = file.read()
tree = html.fromstring(page_content)

# Find all thread elements
threads = tree.xpath('//div[contains(@class, "MessageCard__cell-")]')

# Initialize a list to store the scraped data
data = []

# Scrape the number of posts in each thread
for thread in threads:
    thread_title = thread.xpath('.//h1[@class="MessageCard__thread-title"]/text()')[0].strip()
    post_count = thread.xpath('.//span[@class="MessageCard__post-count"]/text()')[0].strip().split()[0]
    data.append((thread_title, post_count))

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Thread Title', 'Post Count'])
    writer.writerows(data)