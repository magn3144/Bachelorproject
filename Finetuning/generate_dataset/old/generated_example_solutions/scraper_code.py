import csv
from bs4 import BeautifulSoup

# Define the HTML file path
html_file_path = "downloaded_pages/reddit.com.html"

# Open the HTML file
with open(html_file_path, "r") as file:
    # Read the contents of the file
    html_contents = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_contents, "html.parser")

# Find the element containing the downvote count
downvote_element = soup.find(class_="icon-downvote")

# Extract the parent element containing the downvote count
downvote_parent_element = downvote_element.parent.parent

# Extract the downvote count
downvote_count = downvote_parent_element.find(class_="_1rZYMD_4xY3gRcSS3p8ODO").text

# Save the downvote count to a CSV file
with open("downvote_count.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Downvote Count"])
    writer.writerow([downvote_count])