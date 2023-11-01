import csv
from lxml import etree

def extract_text_from_element(tree, xpath):
    elements = tree.xpath(xpath)
    text = [element.text.strip() for element in elements]
    return text

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Category', 'Text'])
        writer.writerows(data)

file_path = 'downloaded_pages/netflix.html'
category_xpath = '/html/body/div[1]/div/div[2]/main/section[2]/h2'
text_xpath = '/html/body/div[1]/div/div[2]/main/section[2]/h2/following-sibling::div/span/span[@class="nm-collections-title-name"]'

# Read HTML file
with open(file_path, 'r') as file:
    html = file.read()

# Parse HTML tree
tree = etree.HTML(html)

# Extract category and text
category = extract_text_from_element(tree, category_xpath)[0]
text = extract_text_from_element(tree, text_xpath)

# Prepare data for CSV
data = [(category, t) for t in text]

# Save data to CSV
save_to_csv(data)