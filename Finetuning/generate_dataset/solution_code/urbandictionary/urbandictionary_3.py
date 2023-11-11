from bs4 import BeautifulSoup
import csv

# Local path to the HTML file
html_file = 'downloaded_pages/urbandictionary.html'

# XPath of the target element
target_xpath = '/html/body/div/div/main/div/div[4]/section/div[3]/div/div[5]/a/span'

# Parse the HTML file
with open(html_file, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find the target element using XPath
target_element = soup.find('a', xpath=target_xpath)

# Get the text of the target element
target_text = target_element.text.strip()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Link', 'XPath'])
    writer.writerow([target_text, target_xpath])