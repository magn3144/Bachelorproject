import csv
from lxml import html

# Function to extract the titles of sponsored posts
def extract_sponsored_titles():
    # Open the HTML file
    with open('downloaded_pages/tumblr.html', 'r') as f:
        # Read the content of the file
        content = f.read()

    # Create an lxml tree from the HTML content
    tree = html.fromstring(content)

    # Find all the sponsored post titles using XPath
    sponsored_titles = tree.xpath("//h1[contains(@class, 'hF8Wr YkQj_')]/text()")

    # Create a list to hold the extracted titles
    titles = []

    # Iterate through the sponsored titles and append them to the list
    for title in sponsored_titles:
        titles.append(title.strip())

    return titles

# Main function to save the extracted data to a CSV file
def save_data_to_csv(data):
    # Create a CSV file named 'scraped_data.csv'
    with open('scraped_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for title in data:
            # Write each title as a row in the CSV file
            writer.writerow([title])

# Extract the titles of sponsored posts
sponsored_titles = extract_sponsored_titles()

# Save the extracted titles to a CSV file
save_data_to_csv(sponsored_titles)
