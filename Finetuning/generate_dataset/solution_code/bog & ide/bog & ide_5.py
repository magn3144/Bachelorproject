from bs4 import BeautifulSoup
import csv

# Specify the local path to the HTML file
html_file_path = "downloaded_pages/bog & ide.html"

# Define the category
category = "Book Websites"

# Define the XPath for the element with the class "css-p69eic-TagItem"
xpath = '/html/body/div/main/div[1]/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div/div/a[1]/div'

# Open the HTML file and parse it with BeautifulSoup
with open(html_file_path, 'r') as file:
    html = file.read()
    soup = BeautifulSoup(html, 'html.parser')

# Find the element using the XPath
element = soup.find('div', class_='css-p69eic-TagItem eokha2j0')

# Extract the text from the element
text = element.text

# Save the extracted text as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow([category, xpath, text])