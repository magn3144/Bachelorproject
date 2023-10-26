import csv
import os
import re
from lxml import etree

# Define the target attributes
target_category = "News"
target_section_title = "Middle East News"

# Define the XPath for the section title
section_title_xpath = '/html/body/div[1]/div/div[3]/div/div[1]/div/h1/div'

# Define the XPath for the article titles
article_title_xpath = '/html/body/div[1]/div/div[3]/div/div[1]/div/div[@class="teaser"]//h2/a'

# Define the local path to the HTML file
html_file_path = 'downloaded_pages/aljazeera.html'

def extract_article_titles():
    # Parse the HTML file
    with open(html_file_path, 'r') as html_file:
        html_data = html_file.read()
        html_tree = etree.HTML(html_data)

    # Get the section title
    section_title = html_tree.xpath(section_title_xpath)[0].text

    # Check if the category and section title match the target
    if target_category.lower() not in section_title.lower() or target_section_title.lower() not in section_title.lower():
        print("Category or section title does not match the target.")
        return

    # Extract the article titles
    article_titles = []
    article_elements = html_tree.xpath(article_title_xpath)
    for element in article_elements:
        article_titles.append(element.text.strip())
    
    return article_titles

def save_to_csv(data):
    # Define the CSV file path
    csv_file_path = 'scraped_data.csv'

    # Check if the file already exists
    file_exists = os.path.isfile(csv_file_path)

    # Open the CSV file in append mode
    with open(csv_file_path, 'a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)

        # Write the header if the file is new
        if not file_exists:
            writer.writerow(['Article Title'])

        # Write the data rows
        for row in data:
            writer.writerow([row])

# Extract the article titles
article_titles = extract_article_titles()

# Save the article titles to CSV file
save_to_csv(article_titles)