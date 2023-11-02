import csv
import requests
from lxml import etree

# Define the target URL and the local path to the HTML file
url = "https://finance.yahoo.com"
local_path = "downloaded_pages/finance.yahoo.html"

# Define the XPaths for the randomly selected HTML elements
xpaths = {
    "options_element": "/html/body/div[1]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/ul/li[13]/a",
    "skip_element": "/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/ul/li[2]/a",
    "search_element": "/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div/form/label",
    "news_element": "/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/ul/li[2]/div/div/div/div[2]/ul/li[29]/a/div/div/p",
    "p_element": "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/ul/li[2]/div/div[1]/div/p",
    "notifications_element": "/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/ul/li[2]/div/div/div/h3",
    "div_element": "/html/body/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div/div/div[2]/div/ul/li[4]/div/div/div/div[2]/div",
    "span_element": "/html/body/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div/div/div[2]/div/ul/li[5]/div/div/div/h3/a/span",
    "percent_element": "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/section/div/div[2]/div[1]/table/tbody/tr[21]/td[5]/fin-streamer/span",
    "today_element": "/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/ul/li[2]/div/div/div/div[1]/h4",
    "price_element": "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/section/div/div[2]/div[1]/table/thead/tr/th[3]",
    "company1_element": "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/section/div/div[2]/div[1]/table/tbody/tr[25]/td[2]",
    "company2_element": "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/section/div/div[2]/div[1]/table/tbody/tr[21]/td[2]",
    "highest_options_element": "/html/body/div[1]/div/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div/ul/li[12]/a",
    "solceller_element": "/html/body/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div/div/div[2]/div/ul/li[14]/div/div[1]/div[2]/a",
    "news_element2": "/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/ul/li[2]/div/div/div/div[2]/ul/li[34]/a/div/div/p",
    "empty_element": "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/ul/li[12]/div/div[1]/div/p",
    "trending_element": "/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div/form/div[2]/div[2]/div/h3",
    "we_element": "/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div/form/div[2]/div[2]/ul/li[3]/div[2]",
    "ticker_element": "/html/body/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div/div/div[2]/div/ul/li[13]/div/div/div/h3/a/span",
    "mail_element": "/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/ul/li[3]/a/span",
    "older_element": "/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/ul/li[2]/div/div/div/div[2]/h4",
    "volume_element": "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/section/div/div[2]/div[1]/table/thead/tr/th[6]",
}

# Create a list of web-scraping tasks
tasks = [
    {"element": "Options", "xpath": xpaths["options_element"]},
    {"element": "Skip to Main Content", "xpath": xpaths["skip_element"]},
    {"element": "Search", "xpath": xpaths["search_element"]},
    {"element": "News", "xpath": xpaths["news_element"]},
    {"element": "Empty Paragraph", "xpath": xpaths["p_element"]},
    {"element": "Notifications", "xpath": xpaths["notifications_element"]},
    {"element": "Div Element", "xpath": xpaths["div_element"]},
    {"element": "Span Element", "xpath": xpaths["span_element"]},
    {"element": "Percent Change", "xpath": xpaths["percent_element"]},
    {"element": "Today", "xpath": xpaths["today_element"]},
    {"element": "Price (Intraday)", "xpath": xpaths["price_element"]},
    {"element": "Company 1", "xpath": xpaths["company1_element"]},
    {"element": "Company 2", "xpath": xpaths["company2_element"]},
    {"element": "Options: Highest Open Interest", "xpath": xpaths["highest_options_element"]},
    {"element": "Solceller.nu", "xpath": xpaths["solceller_element"]},
    {"element": "News 2", "xpath": xpaths["news_element2"]},
    {"element": "Empty Paragraph 2", "xpath": xpaths["empty_element"]},
    {"element": "Trending Tickers", "xpath": xpaths["trending_element"]},
    {"element": "WE", "xpath": xpaths["we_element"]},
    {"element": "Fed decision, ADP data, earnings", "xpath": xpaths["ticker_element"]},
    {"element": "Mail", "xpath": xpaths["mail_element"]},
    {"element": "Older", "xpath": xpaths["older_element"]},
    {"element": "Volume", "xpath": xpaths["volume_element"]},
]


def scrape_element(url, xpath):
    response = requests.get(url)
    html = response.content
    tree = etree.HTML(html)
    element = tree.xpath(xpath)
    if len(element) > 0:
        return element[0].text
    else:
        return ""


# Scrape the data for each task and save it to a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Element", "Data"])
    for task in tasks:
        element = task["element"]
        xpath = task["xpath"]
        data = scrape_element(url, xpath)
        writer.writerow([element, data])