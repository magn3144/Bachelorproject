import csv
from lxml import html

# Open the HTML file
with open('downloaded_pages/ebay.html', 'r') as file:
    html_content = file.read()

#Parse the html content
tree = html.fromstring(html_content)

# Find the "Sign in" link using the XPath
link_element = tree.xpath('/html/body/div[3]/header/div/ul[2]/li[3]/div/div[1]/div/div[2]/span/a')[0]
user_information = link_element.text

# Write the scraped data to a CSV file
csv_data = [['User Information']]
csv_data.append([user_information])

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)