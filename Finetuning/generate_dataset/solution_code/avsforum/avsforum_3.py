import csv
from lxml import html

# Read the HTML file
with open('downloaded_pages/avsforum.html', 'r') as file:
    html_content = file.read()

# Parse the HTML
tree = html.fromstring(html_content)

# Extract the text of the links in the "Top Contributors this Month" section
contributors = tree.xpath("//h3[contains(@class, 'title') and text()='Top Contributors this Month']")
if contributors:
    section = contributors[0].getparent().xpath("./following-sibling::ul[1]")
    if section:
        links = section[0].xpath(".//a")
        scraped_data = [link.text_content().strip() for link in links]
        scraped_data = [link for link in scraped_data if link]  # Remove any empty links

        # Save the scraped data as a CSV file
        with open('scraped_data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(('Contributor',))
            writer.writerows([link] for link in scraped_data)