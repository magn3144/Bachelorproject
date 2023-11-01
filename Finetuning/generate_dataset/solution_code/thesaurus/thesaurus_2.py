import csv
from lxml import etree

# Define the XPath expressions for the elements we need
category_xpath = '/html/body/div/div/main/div[1]/nav/a[2]'
word_xpath = '//a[contains(@class, "swOceu30Ur0oywqmOgSd")]'

# Function to scrape the ghost-related words and their meanings
def scrape_ghost_words(html_file):
    # Parse the HTML file
    tree = etree.parse(html_file)

    # Find the category of the page
    category = tree.xpath(category_xpath)[0].text

    # Find all the ghost-related words and their meanings
    words = []
    for element in tree.xpath(word_xpath):
        word = element.text.strip()
        words.append(word)

    return category, words

# Scraping the data
category, ghost_words = scrape_ghost_words("downloaded_pages/thesaurus.html")

# Saving the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Category", "Word"])
    writer.writerow([category, ""])  # Empty row for better readability
    for word in ghost_words:
        writer.writerow([category, word])