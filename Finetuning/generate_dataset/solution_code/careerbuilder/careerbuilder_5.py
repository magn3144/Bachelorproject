import csv
from lxml import etree

# Define the XPaths for the recommendations
recommendations_xpaths = [
    "/html/body/div[1]/div/div[2]/main/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/span[2]",
    "/html/body/div[1]/div/div[2]/main/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/span[3]",
    "/html/body/div[1]/div/div[2]/main/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/span[4]"
]

# Load the HTML file
tree = etree.parse("downloaded_pages/careerbuilder.html")

# Create a list to store the recommendations
recommendations = []

# Extract the recommendations from the HTML using the defined XPaths
for xpath in recommendations_xpaths:
    recommendation = tree.xpath(xpath)
    if recommendation:
        recommendations.append(recommendation[0].text)

# Write the recommendations to a CSV file
with open("scraped_data.csv", "w") as file:
    writer = csv.writer(file)
    for recommendation in recommendations:
        writer.writerow([recommendation])