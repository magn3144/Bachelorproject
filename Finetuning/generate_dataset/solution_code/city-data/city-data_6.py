import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/city-data.html', 'r') as f:
    content = f.read()

# Parse the HTML content
tree = html.fromstring(content)

# Extract the text from the <h3> element
h3_element = tree.xpath('/html/body/div[3]/div[4]/div[2]/div/h3')[0]
text = h3_element.text_content()

# Write the extracted text to a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Extracted Text'])
    writer.writerow([text])

print("Data scraped successfully and saved as 'scraped_data.csv'")