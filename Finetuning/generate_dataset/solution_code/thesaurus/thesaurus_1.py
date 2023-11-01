import csv
from lxml import etree

# Open the HTML file and read its contents
with open('downloaded_pages/thesaurus.html', 'r') as file:
    html = file.read()

# Parse the HTML content
tree = etree.HTML(html)

# Find the featured games and their descriptions
game_elements = tree.xpath("//h2[contains(@class, 'bGXYJrRLH25ON04NlCTo') and text()='Games']/"
                           "following-sibling::div[contains(@class, 'Vmn3EDTx8gXJ1BOikE9Q')]/a")
descriptions = tree.xpath("//h2[contains(@class, 'bGXYJrRLH25ON04NlCTo') and text()='Games']/"
                          "following-sibling::div[contains(@class, 'Vmn3EDTx8gXJ1BOikE9Q')]/p")

# Create a list of dictionaries containing the scraped data
scraped_data = []
for game_element, description in zip(game_elements, descriptions):
    game_name = game_element.text.strip()
    game_description = description.text.strip()
    scraped_data.append({'Game Name': game_name, 'Description': game_description})

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Game Name', 'Description'])
    writer.writeheader()
    writer.writerows(scraped_data)