import csv
import lxml.html

# Load the HTML file
html_file = "downloaded_pages/cbsports.html"
tree = lxml.html.parse(html_file)

# Find all labels in the HTML tree
labels = tree.xpath("//label")

# Extract the text from each label and save it to a list
label_texts = [label.text_content().strip() for label in labels]

# Save the label texts as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Label"])
    writer.writerows([[text] for text in label_texts])