import csv
from lxml import etree

# Define the target file path
file_path = "downloaded_pages/bloggersroad.html"

# Define the XPath expressions for the blog titles
blog_title_xpaths = [
    "/html/body/div/div[1]/div/main/div/article/div/header/h2/a",
    "/html/body/div/div[1]/div/main/div/article[2]/div/header/h2/a",
    "/html/body/div/div[1]/div/main/div/article[3]/div/header/h2/a",
    "/html/body/div/div[1]/div/main/div/article[4]/div/header/h2/a"
]

# Create a function to extract the blog titles and their corresponding XPaths
def extract_blog_titles(file_path, blog_title_xpaths):
    # Parse the HTML file
    tree = etree.parse(file_path)

    # Initialize a list to store the extracted data
    scraped_data = []

    # Extract the blog titles and their corresponding XPaths
    for xpath in blog_title_xpaths:
        elements = tree.xpath(xpath)
        for element in elements:
            title = element.text.strip()
            scraped_data.append([title, xpath])

    return scraped_data

# Extract the blog titles and their corresponding XPaths
data = extract_blog_titles(file_path, blog_title_xpaths)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'XPath'])
    writer.writerows(data)