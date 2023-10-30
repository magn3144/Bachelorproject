import csv
import lxml.html

# Read the HTML file
with open('downloaded_pages/wordpress.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML
tree = lxml.html.fromstring(html_content)

# Find the element with text "The Line Hotels"
element_text = tree.xpath("/html/body/div/div[3]/div[2]/a/span[2]")[0].text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([element_text])