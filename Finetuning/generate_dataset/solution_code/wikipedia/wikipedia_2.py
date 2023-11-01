import csv
import os
import re
from lxml import etree

# Function to extract the text from an element based on its XPath
def extract_text(element, xpath):
    result = element.xpath(xpath)
    if result:
        return result[0].text.strip()
    return ''

# Function to extract the headline of the featured list
def extract_featured_list_headline(root):
    xpath = '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[3]/h2/span[2]'
    return extract_text(root, xpath)

# Function to save the scraped data as a CSV file
def save_to_csv(data):
    file_name = 'scraped_data.csv'
    file_exists = os.path.exists(file_name)
    
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Category', 'Headline'])
        writer.writerow(data)

# Main scraping function
def scrape_website():
    with open('downloaded_pages/wikipedia.html', 'r') as file:
        html = file.read()
    root = etree.HTML(html)

    featured_list_headline = extract_featured_list_headline(root)
    data = ['Educational Websites', featured_list_headline]
    save_to_csv(data)

# Run the scraping function
scrape_website()