import csv
from lxml import html

# Load the HTML file
with open('downloaded_pages/trustpilot.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Define the xpath expressions for the insurance company ratings
xpath_expressions = ['/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div[4]/a/div[3]/div/div/p[2]',
                     '/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div[6]/a/div[3]/div/div/p[2]',
                     '/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div[7]/a/div[3]/div/div/p[2]']

# Extract the ratings
ratings = []
for expression in xpath_expressions:
    rating_element = tree.xpath(expression)
    if rating_element:
        ratings.append(rating_element[0].text.strip())
    else:
        ratings.append('N/A')

# Get the insurance company names from the XPaths
company_names = []
for expression in xpath_expressions:
    company_name_element = tree.xpath(expression + "/../../../div/div/a/div[2]/span")
    if company_name_element:
        company_names.append(company_name_element[0].text.strip())
    else:
        company_names.append('N/A')

# Calculate the average ratings
average_ratings = []
for rating in ratings:
    if rating.isdigit():
        average_ratings.append(int(rating))
    else:
        average_ratings.append(0)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Company Name', 'Average Rating'])
    for i in range(len(company_names)):
        writer.writerow([company_names[i], average_ratings[i]])