import csv
from bs4 import BeautifulSoup

html_file = "downloaded_pages/reddit.com.html"

# Read the HTML file
with open(html_file, "r") as f:
    html_data = f.read()

soup = BeautifulSoup(html_data, "html.parser")

# Find all comment elements
comments = soup.find_all("div", class_="_1poyrkZ7g36PawDueRza-J")

# Extract the comment text
comment_texts = [comment.text for comment in comments]

# Save the comments as CSV file
with open("reddit_comments.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Comment"])
    writer.writerows(zip(comment_texts))