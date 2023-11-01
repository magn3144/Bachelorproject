import csv
from lxml import html

# Define the target file path
file_path = "downloaded_pages/textures.html"

# Define the XPaths for the texture creation dates
texture_date_xpath = "//div[@class='texture-creation-date']"

# Initialize a list to store the scraped data
scraped_data = []

# Parse the HTML file
tree = html.parse(file_path)

# Extract the texture creation dates using XPath
texture_dates = tree.xpath(texture_date_xpath)

# Iterate over the texture dates and append them to the scraped data list
for texture_date in texture_dates:
    date = texture_date.text.strip() if texture_date.text else ""
    scraped_data.append(date)

# Define the output file name
output_file = "scraped_data.csv"

# Write the scraped data to a CSV file
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Texture Creation Date"])
    writer.writerows(zip(scraped_data))