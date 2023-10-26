import csv
from lxml import etree

# Read the HTML file
with open('downloaded_pages/avsforum.html', 'r') as file:
    html = file.read()

# Create an ElementTree object from the HTML
tree = etree.HTML(html)

# Find the Recommended Communities section
recommended_communities = tree.xpath("//div[@class='title' and text()='Recommended Communities']")

if recommended_communities:
    communities_section = recommended_communities[0].getparent()
    communities = communities_section.findall(".//a")

    # Extract the text of each community
    community_names = []
    for community in communities:
        community_names.append(community.text.strip())

    # Save the scraped data as a CSV file
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Recommended Communities'])
        writer.writerows([[name] for name in community_names])