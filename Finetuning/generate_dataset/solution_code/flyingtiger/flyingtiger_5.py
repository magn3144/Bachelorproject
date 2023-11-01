import csv
from lxml import html

# Define the file path
file_path = "downloaded_pages/flyingtiger.html"

# Define the XPaths for the <h2> tags
xpaths = [
    "/html/body/main/div[6]/div/div/div/a/div/div/div/div[2]/div/h2",
    "/html/body/main/section[6]/div/div/div/h2",
    "/html/body/main/section[9]/div/ugc-slider/div/div/h3",
    "/html/body/div[1]/div[2]/sticky-header/header/nav/ul/li[15]/header-menu/div/div/div/div/div[2]/div[1]/div/h3",
    "/html/body/main/section[6]/div/div/slider-component/ul/li[11]/a/h4",
    "/html/body/div[1]/div[2]/sticky-header/header/drawer-component/div/div[2]/div[2]/div/div/div/nav/ul/li[3]/details/div/div/div[2]/div[1]/p",
    "/html/body/main/section[3]/div/div/slider-component/ul/li[2]/div/div/div[1]/div[2]/modal-opener/button/a/span",
    "/html/body/div[1]/div[2]/sticky-header/header/drawer-component/div/div[2]/div[2]/div/div/div/nav/ul/li[13]/details/div/div/div[1]/a/div/h3"
]

# Extract the text from the specified XPaths
scraped_data = []
tree = html.parse(file_path)
for xpath in xpaths:
    element = tree.xpath(xpath)
    if element:
        text = element[0].text.strip()
        scraped_data.append(text)

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Scraped Data"])
    writer.writerows(zip(scraped_data))

print("Scraping complete! The data has been saved in 'scraped_data.csv'.")