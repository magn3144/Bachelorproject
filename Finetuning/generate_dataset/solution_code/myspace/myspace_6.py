from bs4 import BeautifulSoup
import csv

# Load the HTML file
with open("downloaded_pages/myspace.html") as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Find all the articles containing Pedicab Interviews
articles = soup.find_all("article", class_="interview")

# Initialize a list to store the descriptions
descriptions = []

# Extract the descriptions from the articles
for article in articles:
    description = article.find("h4", class_="description").text
    descriptions.append(description)

# Save the descriptions as a CSV file
with open("scraped_data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Description"])
    writer.writerows(zip(descriptions))

print("Data has been successfully scraped and saved as scraped_data.csv")