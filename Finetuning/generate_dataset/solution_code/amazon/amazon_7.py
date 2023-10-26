import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/amazon.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
html_tree = etree.HTML(html_content)

# Find the sorting dropdown menu element
sorting_dropdown_xpath = '/html/body/div[1]/div[1]/span[2]/div/h1/div/div[4]/div/div/form/span/label/select'
sorting_dropdown = html_tree.xpath(sorting_dropdown_xpath)[0]

# Get all the options in the sorting dropdown menu
options = sorting_dropdown.xpath('.//option')

# Retrieve the option text for each option
option_text_list = [option.text.strip() for option in options]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Option'])
    for option_text in option_text_list:
        writer.writerow([option_text])