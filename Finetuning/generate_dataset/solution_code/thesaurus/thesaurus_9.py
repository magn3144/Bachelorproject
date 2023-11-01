import csv
from lxml import html

# Define the target file path and URL
file_path = "downloaded_pages/thesaurus.html"
url = "https://www.thesaurus.com/"

# Read the HTML file and create an XPath tree
with open(file_path, "r") as file:
    html_content = file.read()
tree = html.fromstring(html_content)

# Scrape the top crossword puzzles and their clues
crossword_elements = tree.xpath("//div[@class='crosswords-panel__puzzle--3l2Pi']/a")
crossword_data = []
for element in crossword_elements:
    crossword = element.text.strip()
    clue = element.xpath("./span/text()")[0].strip()
    crossword_data.append((crossword, clue))

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Crossword", "Clue"])  # Write header
    for data in crossword_data:
        writer.writerow(data)