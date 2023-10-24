import csv
from lxml import etree

# Define the XPath expressions for the numeric figures
numeric_xpath_expressions = [
    "/html/body//text()[normalize-space(.) and contains(translate(., '1234567890.', ''), '')]/normalize-space(.)"
]

# Function to extract numeric figures from the HTML using XPath expressions
def extract_numeric_figures(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()
    
    tree = etree.HTML(html)
    
    numeric_figures = []
    for expression in numeric_xpath_expressions:
        results = tree.xpath(expression)
        for result in results:
            numeric_figures.append(result.strip())
    
    return numeric_figures

# Path to the downloaded HTML file
html_file_path = 'downloaded_pages/reddit.html'

# Extract the numeric figures from the HTML
numeric_figures = extract_numeric_figures(html_file_path)

# Write the numeric figures to a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for figure in numeric_figures:
        writer.writerow([figure])