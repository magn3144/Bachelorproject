import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/stackexchange-hot-questions.html', 'r') as file:
    html_string = file.read()

# Parse the HTML string
tree = html.fromstring(html_string)

# Get all the question links
question_links = tree.xpath('//a[@class="question-link"]/text()')

# Save the question links as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Question'])
    writer.writerows(zip(question_links))