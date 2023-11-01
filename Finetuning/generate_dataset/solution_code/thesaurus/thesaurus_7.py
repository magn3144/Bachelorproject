import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/thesaurus.html', 'r') as file:
    html_data = file.read()

# Parse the HTML
tree = html.fromstring(html_data)

# Extract the names and descriptions of horror-related games
game_names = tree.xpath('/html/body/div/div/main/div[1]/div[5]/div[1]/div/h2/text()')
game_descriptions = tree.xpath('/html/body/div/div/main/div[1]/div[5]/div[1]/div/p/text()')

# Combine the names and descriptions into a list of tuples
game_data = list(zip(game_names, game_descriptions))

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Description'])  # Write header row
    writer.writerows(game_data)  # Write data rows