import csv
from lxml import etree

# Define the target file path
filename = 'downloaded_pages/wikipedia.html'

# Read the HTML file
with open(filename, 'r') as file:
    html_data = file.read()

# Create an XML parser
parser = etree.HTMLParser()
tree = etree.fromstring(html_data, parser)

# Find all the elements containing country names using their XPaths
country_elements = tree.xpath('''//a[contains(text(), "Afghanistan")] |
                                 //a[contains(text(), "Albania")] |
                                 //a[contains(text(), "Algeria")] |
                                 //a[contains(text(), "Andorra")] |
                                 //a[contains(text(), "Angola")] |
                                 //a[contains(text(), "Antigua and Barbuda")] |
                                 //a[contains(text(), "Argentina")] |
                                 //a[contains(text(), "Armenia")] |
                                 //a[contains(text(), "Australia")] |
                                 //a[contains(text(), "Austria")] |
                                 //a[contains(text(), "Azerbaijan")] |
                                 //a[contains(text(), "Bahamas")] |
                                 //a[contains(text(), "Bahrain") and not(contains(text(), "Blackburn"))] |
                                 //a[contains(text(), "Bangladesh")] |
                                 //a[contains(text(), "Barbados")] |
                                 //a[contains(text(), "Belarus")] |
                                 //a[contains(text(), "Belgium")] |
                                 //a[contains(text(), "Belize")] |
                                 //a[contains(text(), "Benin")]]''')

# Extract the country names from the elements
countries = [element.text for element in country_elements]

# Save the country names to a CSV file
file_path = 'scraped_data.csv'
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Country'])
    writer.writerows([[country] for country in countries])