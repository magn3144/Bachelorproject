import csv
from bs4 import BeautifulSoup
import requests

# Define the local path to the HTML file
html_file_path = "downloaded_pages/careerbuilder.html"

# Define the URL of the page
url = "https://www.careerbuilder.com/"

# Send a GET request to the page and get the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all div elements in the HTML content
div_elements = soup.find_all("div")

# Extract the text from each div element
scraped_data = [div.get_text().strip() for div in div_elements]

# Write the scraped data to a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Scraped Data"])
    writer.writerows([[data] for data in scraped_data])