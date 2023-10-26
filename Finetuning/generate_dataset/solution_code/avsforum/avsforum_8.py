import csv
from lxml import etree

# Load HTML file
html_path = "downloaded_pages/avsforum.html"
with open(html_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse HTML content
html_tree = etree.HTML(html_content)

# Find the target element using XPath
target_xpath = "/html/body/div[1]/div[4]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]"
target_element = html_tree.xpath(target_xpath)[0]

# Extract the text from the target element
target_text = target_element.text.strip()

# Save the scraped data as a CSV file
csv_path = "scraped_data.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Explore Our Forums"])
    writer.writerow([target_text])

print("Scraping completed and data saved as 'scraped_data.csv'.")