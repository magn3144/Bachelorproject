import csv
import lxml.html

# Define the file path
path = 'downloaded_pages/reddit.html'

# Read the HTML file
with open(path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
html_tree = lxml.html.fromstring(html_content)

# Extract the number of comments
comment_xpath = '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[5]/div/div/div/div[138]/div/div/div/div[2]/div[2]/div[1]/span/a'
comment_element = html_tree.xpath(comment_xpath)[0]
comments = comment_element.text

# Save the scraped data as CSV
data = [['Number of Comments']]
data.append([comments])

with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)