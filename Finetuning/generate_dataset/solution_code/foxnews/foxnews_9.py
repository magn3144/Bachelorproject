import csv
from lxml import etree

# Define the XPath expressions
about_xpath = "/html/body/div/footer/div[1]/div/nav[h4[@class='nav-title']='About']//text()"
other_xpath = "/html/body/div/footer/div[1]/div/nav[h4[@class='nav-title']='Other']//text()"

# Load the HTML file
tree = etree.parse('downloaded_pages/foxnews.html')

# Scrape the text of 'About' and 'Other' sections
about_text = tree.xpath(about_xpath)
other_text = tree.xpath(other_xpath)

# Combine the scraped data
scraped_data = [('About', ' '.join(about_text)), ('Other', ' '.join(other_text))]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Section', 'Text'])
    writer.writerows(scraped_data)