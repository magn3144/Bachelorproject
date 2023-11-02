import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/finance.yahoo.html', 'r') as f:
    html_content = f.read()

# Parse the HTML content
tree = html.fromstring(html_content)

# Find the required elements using XPaths
fed_decision = tree.xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[2]/div/div/div/div/div/div[2]/div/ul/li[13]/div/div/div/h3/a/span')
adp_data = tree.xpath('/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/ul/li[2]/div/div/div/div[1]/h4')
earnings = tree.xpath('/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div/form/div[2]/div[1]/div/h3')

# Extract the text from the elements
fed_decision_text = fed_decision[0].text_content() if fed_decision else ''
adp_data_text = adp_data[0].text_content() if adp_data else ''
earnings_text = earnings[0].text_content() if earnings else ''

# Save the scraped data as a CSV file
data = [
    ['Fed Decision', fed_decision_text],
    ['ADP Data', adp_data_text],
    ['Earnings', earnings_text]
]

with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)