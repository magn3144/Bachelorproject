import csv
from lxml import etree

# Define the target page file path
file_path = 'downloaded_pages/bodybuilding.html'

# Define the category
category = 'Forums and Review Sites'

# Define the HTML elements and their XPaths
elements = [
    {
    'text': 'Kris Gethin Muscle Building',
    'xpath': '/html/body/section/main/div[3]/div[2]/div/div/div/div/div[2]/div/div[29]/figure/a/figcaption/div[1]/span'
    },
    {
    'text': 'Your Transformation Starts Here Volume 2',
    'xpath': '/html/body/section/main/div[4]/div[2]/div/div/div/div/div[2]/div/div[5]/figure/a/figcaption/div[1]/span'
    },
    {
    'text': 'Foundations of Nutrition',
    'xpath': '/html/body/section/main/div[5]/div[2]/div/div/div/div/div[2]/div/div[31]/figure/a/figcaption/div[1]/span'
    },
    {
    'text': 'Serious Strength in 8 Weeks',
    'xpath': '/html/body/section/main/div[5]/div[2]/div/div/div/div/div[2]/div/div[22]/figure/a/figcaption/div[1]/span'
    },
    {
    'text': 'Full-Body Weight-Loss Home Workouts',
    'xpath': '/html/body/section/main/div[5]/div[2]/div/div/div/div/div[2]/div/div[20]/figure/a/figcaption/div[1]/span'
    },
    {
    'text': 'Livefit',
    'xpath': '/html/body/section/main/div[4]/div[2]/div/div/div/div/div[2]/div/div[18]/figure/a/figcaption/div[1]/span'
    },
    {
    'text': 'Muscle Building',
    'xpath': '/html/body/section/main/div[3]/div[1]/div/h2'
    }
]

# Function to scrape plan descriptions and their corresponding XPaths
def scrape_plan_descriptions(file_path, elements):
    # Parse the HTML file
    parser = etree.HTMLParser()
    tree = etree.parse(file_path, parser)

    # Create a list to store the scraped data
    scraped_data = []

    # Scrape plan descriptions and their corresponding XPaths
    for element in elements:
        text = element['text']
        xpath = element['xpath']
        description = tree.xpath(xpath)[0].text.strip()
        scraped_data.append([text, description])

    # Save the scraped data as a CSV file
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Plan', 'Description'])
        writer.writerows(scraped_data)

# Call the scrape_plan_descriptions function
scrape_plan_descriptions(file_path, elements)