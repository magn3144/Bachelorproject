import csv
from lxml import html

# Web page details
category = "Blogs"
target_page = "wordpress"
html_file_path = "downloaded_pages/wordpress.html"

# XPaths
more_about_section_xpath = "/html/body/div/main/div[2]/div/div[2]/div/h2"

# Function to retrieve text using XPath
def get_text(xpath, tree):
    element = tree.xpath(xpath)
    if element:
        return element[0].text_content().strip()
    return ""

# Parse HTML file
with open(html_file_path, "r", encoding="utf-8") as file:
    html_content = file.read()
    tree = html.fromstring(html_content)

# Retrieve the title of the "More about this site" section
more_about_title = get_text(more_about_section_xpath, tree)

# Save scraped data as CSV
data = [["Category", "Page", "More About Title"]]
data.append([category, target_page, more_about_title])

with open("scraped_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)