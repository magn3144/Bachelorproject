import csv
from lxml import etree

# Open the HTML file
with open('downloaded_pages/jysk.html', 'r') as f:
    html_content = f.read()

# Parse the HTML content
html_tree = etree.HTML(html_content)

# Get the phone number
phone_number_element = html_tree.xpath('/html/body/div[1]/div/div[3]/div[4]/footer/div/div/div[4]/div[2]/div/div/p[1]/a')[0]
phone_number = phone_number_element.text.strip()

# Get the fax number
fax_element = html_tree.xpath('/html/body/div[1]/div/div[3]/div[4]/footer/div/div/div[4]/div[2]/div/div/p[1]/a/following-sibling::text()')[0].strip()
fax = fax_element.split()[1]

# Save the scraped data as a CSV file
data = [['Phone Number', 'Fax'], [phone_number, fax]]
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)