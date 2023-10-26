import csv
from lxml import etree

# Define the XPaths for each element
xpaths = {
    "Newfoundland and Labrador": "/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/div/gg-forum-listings/gg-forum-section-list[10]/section/ul/li[3]/gg-forum-listing/div/div[2]/div/a[5]",
    "WA (Perth)": "/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/div/gg-forum-listings/gg-forum-section-list[10]/section/ul/li[5]/gg-forum-listing/div/div[2]/div/a[6]",
    "Submit bug reports": "/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/div/gg-forum-listings/gg-forum-section-list[4]/section/ul/li[6]/gg-forum-listing/div/p/span",
    "Threads": "/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/div/gg-forum-listings/gg-forum-section-list[10]/section/ul/li[4]/gg-forum-listing/div/div[1]/dl/div[1]/dt/span",
    "Footer Links": "/html/body/gg-app/div/gg-footer/footer/div/div/div[1]/h1",
    "Search for your favorite game": "/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/div/gg-forum-listings/gg-forum-search-aside/aside/div/gg-search-container/gg-search/form/label",
    "Search": "/html/body/gg-app/div/gg-header/header/nav/div/gg-header-search/gg-search-container/gg-search/form/label",
    "Looking for a specific game forum?": "/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/div/gg-forum-listings/gg-forum-search-aside/aside/h2",
    "Policies": "/html/body/gg-app/div/gg-footer/footer/div/div/div[3]/h2",
    "Replies": "/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/gg-forum-sidebar/div/div[3]/dl/div[2]/dt",
    "Your Cookie Privacy Options": "/html/body/div[3]/div/div[3]/div/div/div/div/div[1]/div[1]",
    "No results available": "/html/body/div[1]",
    "Policy Info": "/html/body/div[3]/div/div[3]/div/div/div/div/div[2]/div[2]/div[2]/table/thead/tr/th[5]",
    "General Google Preferences": "/html/body/div[3]/div/div[3]/div/div/div/div/div[2]/div[4]/div[2]/table/tbody/tr[2]/td[4]",
    "User Login": "/html/body/div[3]/div/div[3]/div/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[4]",
    "The Witcher: Path Of Destiny": "/html/body/gg-app/div/main/div/gg-sidebar/div/div[3]/div/gg-hotness/gg-hotness-items/ul/li[47]/div/h2/a",
    "Nucleum": "/html/body/gg-app/div/main/div/gg-sidebar/div/div[3]/div/gg-hotness/gg-hotness-items/ul/li[4]/div/h2/a",
    "Held during Memorial Day weekend": "/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/div/gg-forum-listings/gg-forum-section-list[5]/section/ul/li[3]/gg-forum-listing/div/p/span",
    "Published": "/html/body/gg-app/div/main/div/gg-sidebar/div/div[3]/div/gg-hotness/gg-hotness-items/ul/li[23]/div/p/span",
    "boardgame geek": "/html/body/gg-app/div/gg-header/header/nav/div/gg-menu-logo/div/a/h1",
    "Search Category": "/html/body/gg-app/div/gg-header/header/nav/div/gg-header-search/gg-search-container/gg-search/form/div[2]/label",
    "Global Stats": "/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/gg-forum-sidebar/div/div[3]/h2",
    "13K": "/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/div/gg-forum-listings/gg-forum-section-list[10]/section/ul/li[4]/gg-forum-listing/div/div[1]/dl/div[1]/dd",
    "We have over 100K game specific forums": "/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/div/gg-forum-listings/gg-forum-search-aside/aside/p",
    "Thumbs": "/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/gg-forum-sidebar/div/div[3]/dl/div[3]/dt",
    "cookies measure how often visitors use our s": "/html/body/div[3]/div/div[3]/div/div/div/div/div[2]/div[3]/div[2]/div",
    "Your Privacy": "/html/body/div[3]/div/div[1]/div/div[1]/div[1]",
    "Name": "/html/body/div[3]/div/div[3]/div/div/div/div/div[2]/div[2]/div[2]/table/thead/tr/th[1]",
    "Fraud Prevention by Payment Processor": "/html/body/div[3]/div/div[3]/div/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr[7]/td[4]",
    "www.recaptcha.net": "/html/body/div[3]/div/div[3]/div/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr[5]/td[2]",
    "Marvel Champions: The Card Game": "/html/body/gg-app/div/main/div/gg-sidebar/div/div[3]/div/gg-hotness/gg-hotness-items/ul/li[45]/div/h2/a",
    "BGG Store": "/html/body/gg-app/div/gg-header/header/nav/div/div[1]/div/div[1]/ul/li[4]/div/div/div/div/span[3]/a",
    "Hang out and shoot the breeze about anything non-g": "/html/body/gg-app/div/main/div/div/gg-forum-browser/gg-forum-browser-ui/div/div/div/gg-forum-listings/gg-forum-section-list[11]/section/ul/li[1]/gg-forum-listing/div/p/span"
}

# Load the HTML file
with open('downloaded_pages/boardgamegeek.html', 'r') as file:
    html = file.read()

# Create an element tree from the HTML
tree = etree.HTML(html)

# Scrape data from the page using XPaths
scraped_data = {}
for element, xpath in xpaths.items():
    data = tree.xpath(xpath)
    if data:
        scraped_data[element] = data[0].text.strip()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Element', 'Text'])
    for element, text in scraped_data.items():
        writer.writerow([element, text])