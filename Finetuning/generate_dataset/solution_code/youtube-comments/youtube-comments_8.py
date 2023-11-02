import csv
from lxml import etree

# Define the target HTML file path
html_file_path = 'downloaded_pages/youtube-comments.html'

# Define the XPaths for the elements
dislikes_xpath = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[107]/ytd-comment-renderer/div[3]/div[2]/div[1]/div[2]/h3/a/span'

# Create empty list to store scraped data
scraped_data = []

# Parse the HTML file
tree = etree.parse(html_file_path)

# Find number of dislikes using XPath
dislikes_element = tree.xpath(dislikes_xpath)
dislikes = dislikes_element[0].text.strip()

# Append the scraped data to the list
scraped_data.append(dislikes)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Dislikes'])
    writer.writerow(scraped_data)