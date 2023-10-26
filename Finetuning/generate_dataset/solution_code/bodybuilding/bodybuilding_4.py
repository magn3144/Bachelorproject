from lxml import etree
import csv

# Modify this with the local path to the HTML file
html_file_path = "downloaded_pages/bodybuilding.html"

# Modify this with the XPath of the plan categories
plan_categories = {
    "Kris Gethin Muscle Building": "/html/body/section/main/div[3]/div[2]/div/div/div/div/div[2]/div/div[29]/figure/a/figcaption/div[1]/span",
    "Your Transformation Starts Here Volume 2": "/html/body/section/main/div[4]/div[2]/div/div/div/div/div[2]/div/div[5]/figure/a/figcaption/div[1]/span",
    "Foundations of Nutrition": "/html/body/section/main/div[5]/div[2]/div/div/div/div/div[2]/div/div[31]/figure/a/figcaption/div[1]/span",
    "Serious Strength in 8 Weeks": "/html/body/section/main/div[5]/div[2]/div/div/div/div/div[2]/div/div[22]/figure/a/figcaption/div[1]/span",
    "Full-Body Weight-Loss Home Workouts": "/html/body/section/main/div[5]/div[2]/div/div/div/div/div[2]/div/div[20]/figure/a/figcaption/div[1]/span",
    "Livefit": "/html/body/section/main/div[4]/div[2]/div/div/div/div/div[2]/div/div[18]/figure/a/figcaption/div[1]/span",
    "Muscle Building": "/html/body/section/main/div[3]/div[1]/div/h2",
    "Advanced": "/html/body/section/main/div[6]/div[1]/div/h2",
    "Lose Weight": "/html/body/section/main/div[4]/div[1]/div/h2",
    "Select Your Plan": "/html/body/section/div[1]/bb-marketing-banner/section/div/div[2]/h2"
}

# Function to extract the text content using XPath
def extract_text(tree, xpath):
    elements = tree.xpath(xpath)
    return [element.text.strip() for element in elements]

html_tree = etree.parse(html_file_path)

# Scrape the plan categories and their corresponding XPaths
scraped_data = []
for category, xpath in plan_categories.items():
    scraped_data.append([category, xpath])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Category', 'XPath'])
    writer.writerows(scraped_data)