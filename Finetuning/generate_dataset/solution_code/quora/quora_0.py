import csv
from lxml import html

# Load the HTML file
tree = html.parse('downloaded_pages/quora.html')

# Find all user names and their corresponding questions
user_names = tree.xpath('//div[@class="user-name"]/text()')
questions = tree.xpath('//div[@class="question"]/text()')

# Combine user names and questions into a list of tuples
data = list(zip(user_names, questions))

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['User', 'Question'])
    writer.writerows(data)