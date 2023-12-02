
import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/airbnb.html', 'r') as f:
    content = f.read()

# Parse the HTML
tree = html.fromstring(content)

# Find the "show more" buttons
show_more_buttons = tree.xpath('//div[@class="_b0zlx4m"]/button[@class="_14lwomh"]')

# Extract the classes of the buttons
button_classes = [button.attrib['class'] for button in show_more_buttons]

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Classes'])
    writer.writerows([button_classes])
