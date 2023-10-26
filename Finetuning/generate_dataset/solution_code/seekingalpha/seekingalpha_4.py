import csv
from lxml import etree

def extract_percentage_change(html_file_path):
    # Read the HTML file
    with open(html_file_path, 'r') as file:
        html_data = file.read()
    
    # Parse the HTML
    parser = etree.HTMLParser()
    tree = etree.fromstring(html_data, parser)
    
    # Find all the percentage change elements using XPath
    percentage_change_elements = tree.xpath('//span[contains(@class, "hk_fU")]')
    
    # Extract the text and remove the "%" symbol
    percentage_changes = [element.text.strip('%') for element in percentage_change_elements]
    
    return percentage_changes

def save_to_csv(data, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Percentage Change"])
        writer.writerows(zip(data))

# Set the local path to the HTML file
html_file_path = "downloaded_pages/seekingalpha.html"

# Extract the percentage change data
percentage_changes = extract_percentage_change(html_file_path)

# Save the data to CSV file
save_to_csv(percentage_changes, "scraped_data.csv")