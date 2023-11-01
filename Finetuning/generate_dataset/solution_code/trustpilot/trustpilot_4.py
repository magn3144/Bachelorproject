import csv
from lxml import etree

# Define the target HTML file path
html_file = 'downloaded_pages/trustpilot.html'

# Define the XPath expressions for the insurance company names
xpath_expressions = [
    '/html/body/div/div/div/main/div/div[2]/div/div[1]/ul/li[6]/a/span',
    '/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div[6]/a/div[2]/span',
    '/html/body/div/div/div/footer/div/div/div[2]/ul/li[4]/a',
    '/html/body/div/div/div/footer/div/div/section[2]/ul/li[7]/a',
    '/html/body/div/div/div/main/div/div[2]/div/div[3]/div/div/div[8]/a/p',
    '/html/body/div/div/div/main/div/div[2]/aside/div[2]/ul/li[2]/a/p',
    '/html/body/div/div/div/main/div/div[2]/aside/div[1]/fieldset[1]/legend',
    '/html/body/div/div/div/main/div/div[2]/div/section/div[2]/div/label',
    '/html/body/div/div/div/footer/div/div/div[2]/div',
    '/html/body/div/div/div/main/div/div[2]/div/section/div[5]/a/div[1]',
    '/html/body/div/div/div/main/div/div[2]/div/div[2]/h2',
    '/html/body/div/div/div/footer/div/div/section[1]/h3',
    '/html/body/div/div/div/main/div/div[2]/aside/div[2]/ul/li[6]/a/span',
    '/html/body/div/div/div/main/div/div[2]/div/div[3]/div/div/div[1]/a/div[2]/span',
    '/html/body/div/div/div/footer/div/div/div[2]/ul/li[3]/a',
    '/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div[4]/a/div[3]/div/div/p[2]',
    '/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div[6]/a/div[3]/div/div/p[2]',
    '/html/body/div/div/div/main/div/div[2]/aside/div[1]/fieldset[2]/legend',
    '/html/body/div/div/div/main/div/div[2]/div/section/div[4]/a/div[1]',
    '/html/body/div/div/div/main/div/div[2]/div/div[3]/h2',
    '/html/body/div/div/div/footer/div/div/section[2]/h3',
    '/html/body/div/div/div/main/div/div[2]/div/div[1]/ul/li[2]/a/span',
    '/html/body/div/div/div/footer/div/div/section[1]/div/dl/div/dd/ul/li[9]/button/span[2]',
    '/html/body/div/div/div/footer/div/div/section[4]/ul/li[1]/a',
    '/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div[8]/a/div[3]/div/div/p[2]',
    '/html/body/div/div/div/main/div/div[2]/div/div[1]/ul/li[4]/a/p',
    '/html/body/div/div/div/main/div/div[2]/aside/div[1]/fieldset[3]/legend',
    '/html/body/div/div/div/footer/div/div/section[5]/h3',
    '/html/body/div/div/div/main/div/div[2]/aside/div[2]/ul/li[2]/a/span',
    '/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div[7]/a/div[2]/span[1]',
    '/html/body/div/div/div/footer/div/div/section[3]/ul/li[2]/a',
    '/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div[7]/a/div[3]/div/div/p[2]'
]

# Create a list to store the insurance company names
insurance_companies = []

# Read the HTML file
with open(html_file, 'r', encoding='utf-8') as f:
    html_data = f.read()

# Parse the HTML using lxml
tree = etree.HTML(html_data)

# Extract the insurance company names using XPath expressions
for xpath_expression in xpath_expressions:
    elements = tree.xpath(xpath_expression)
    for element in elements:
        insurance_companies.append(element.text.strip())

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Insurance Company Name'])
    writer.writerows([[name] for name in insurance_companies])