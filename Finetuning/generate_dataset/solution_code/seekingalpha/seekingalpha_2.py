import csv
import requests
from lxml import etree

# Define the URL and XPaths
url = "https://seekingalpha.com/market-news"
xpaths = [
    ("/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[2]/section/div/div/div/div[2]/article[110]/div/div/footer/a", "comments"),
    ("/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[2]/section/div/div/div/div[2]/article[49]/div/div/footer/a", "comments"),
    ("/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[2]/section/div/div/div/div[2]/article[9]/div/div/footer/span[2]", "comments"),
    ("/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[1]/div/div[2]/section/div/div[1]/div/div/h1", "Category"),
    ("/html/body/div[2]/div/div[1]/div/header/div[1]/div[1]/div/div/div/span", "Header"),
    ("/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[2]/section/div/div/div/div[2]/article[29]/div/div/footer/a", "comments"),
    ("/html/body/div[2]/div/div[1]/div/header/div[1]/div[2]/div[4]/div/div/div/ul/li[3]/a", "Profile"),
    ("/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[1]/div/div[2]/section/div/div[2]/ul/li[8]/div/a/span/span", "Element 1"),
    ("/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[2]/section/div/div/div/div[2]/article[45]/div/div/h3/a", "comments"),
    ("/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[2]/section/div/div/div/div[2]/article[89]/div/div/footer/a", "comments"),
    ("/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[2]/section/div/div/div/div[2]/article[76]/div/div/footer/span[2]", "comments"),
    ("/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[2]/section/div/div/div/div[2]/article[86]/div/div/h3/a", "comments"),
    ("/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[2]/section/div/div/div/div[2]/article[29]/div/div/footer/a", "comments"),
    ("/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[2]/section/div/div/div/div[2]/article[142]/div/div/h3/a", "comments"),
    ("/html/body/div[2]/div/div[1]/div/header/div[1]/div[2]/div[4]/div/div/div/ul/li[3]/a", "Element 2"),
    ("/html/body/div[2]/div/div[2]/div/div/div[2]/div[1]", "Message"),
    ("/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[2]/section/div/div/div/div[2]/article[29]/div/div/h3/a", "comments"),
    ("/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[2]/section/div/div/div/div[2]/article[123]/div/div/footer/a", "comments"),
    ("/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[2]/section/div/div/div/div[2]/article[142]/div/div/footer/span[2]", "comments"),
    ("/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[1]/div/div[2]/section/div/div[2]/ul/li[8]/div/a/span/span", "Element 3"),
    ("/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[2]/section/div/div/div/div[2]/article[80]/div/div/footer/span[1]/a/span[2]", "Price"),
    ("/html/body/div[2]/div/div[1]/div/header/div[1]/div[2]/div[4]/div/div/div/ul/li[3]/a", "Element 4"),
    ("/html/body/div[2]/div/div[1]/div/main/div[3]/div/div[2]/section/div/div/div/div[2]/article[26]/div/div/footer/a", "comments"),
]

# Create a list to store the scraped data
data = []

# Function to scrape the number of comments for each news article
def scrape_comments(url):
    response = requests.get(url)
    html = response.content
    tree = etree.HTML(html)
    for xpath, comment_id in xpaths:
        comments = tree.xpath(xpath)
        if comments:
            num_comments = comments[0].text.strip().split()[0]
            data.append([comment_id, num_comments])

# Scrape the comments for each news article
scrape_comments(url)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Comment ID', 'Number of Comments'])
    writer.writerows(data)