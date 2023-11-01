import csv
from lxml import html

# Define the XPaths and their corresponding text labels
xpaths = [
    ('/html/body/header/div[5]/div/div[5]/label/div', 'Indkøbskurv')
]

def scrape_data():
    # Load the HTML file
    filename = 'downloaded_pages/elgiganten.html'
    with open(filename, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Parse the HTML content
    tree = html.fromstring(html_content)

    # Scrape the data using the defined XPaths
    data = []
    for xpath, label in xpaths:
        elements = tree.xpath(xpath)
        if elements:
            text = elements[0].text_content().strip()
            data.append((label, text))
        else:
            data.append((label, ''))

    return data

def save_data(data):
    # Save the scraped data as a CSV file
    with open('scraped_data.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Label', 'Text'])
        writer.writerows(data)

# Scrape and save the data
data = scrape_data()
save_data(data)