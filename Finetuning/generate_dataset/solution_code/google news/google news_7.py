import csv
from bs4 import BeautifulSoup

# Define the target HTML file path
html_file_path = "downloaded_pages/google news.html"

# Define the category
category = "News"

# Define the task
task = "Extract the text and corresponding XPaths of all the <a> tags with class 'brSCsc'"

# Read the HTML file
with open(html_file_path, "r") as html_file:
    html_content = html_file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, "html.parser")

# Find all <a> tags with class "brSCsc"
a_tags = soup.find_all("a", class_="brSCsc")

# Initialize a list to store the data
data = [["Text", "XPath"]]

# Extract the text and corresponding XPaths of the <a> tags
for a_tag in a_tags:
    text = a_tag.get_text()
    xpath = soup.find(string=text).find_parent().xpath()
    data.append([text, xpath])

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)