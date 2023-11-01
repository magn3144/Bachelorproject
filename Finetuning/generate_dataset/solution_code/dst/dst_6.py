import csv
from lxml import etree

# Load the HTML file
html_file = "downloaded_pages/dst.html"
with open(html_file, "rb") as file:
    html_content = file.read()

# Parse the HTML content
parser = etree.HTMLParser()
tree = etree.parse(html_file, parser)

# Scrape the divorce statistics by duration of the marriage
divorce_stats_elements = tree.xpath("//h2[@class='selected_statistics_header' and contains(text(),'Divorces by duration of the marriage')]/following-sibling::div")

# Extract the statistics and write them to a CSV file
with open("scraped_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Duration", "Number of Divorces"])

    for stats_element in divorce_stats_elements:
        duration = stats_element.xpath("normalize-space(div[@class='keyword_box_period'])")
        number_of_divorces = stats_element.xpath("normalize-space(span[@class='KeyBoxNumber__Number'])")
        writer.writerow([duration, number_of_divorces])