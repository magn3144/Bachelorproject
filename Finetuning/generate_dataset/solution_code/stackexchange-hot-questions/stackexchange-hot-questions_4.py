import csv
from lxml import html

# Path to the HTML file
path = "downloaded_pages/stackexchange-hot-questions.html"

# XPaths for the Science Fiction & Fantasy sites
xpaths = [
    '/html/body/div/section/div/div[3]/div[2]/div[10]/div/span[2]',
    '/html/body/div/section/div/div[3]/div[2]/div[5]/div/span[2]'
]

# Function to parse the HTML file and extract site names
def parse_html():
    # Parse the HTML file
    with open(path, 'r') as file:
        content = file.read()
        tree = html.fromstring(content)

    site_names = []

    # Extract site names using XPaths
    for xpath in xpaths:
        elements = tree.xpath(xpath)
        site_names.extend([element.text.strip() for element in elements if element.text])

    return site_names

# Function to save the scraped data as CSV
def save_csv(site_names):
    with open('scraped_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Site Names'])
        writer.writerows([[name] for name in site_names])

# Main function
def main():
    site_names = parse_html()
    save_csv(site_names)

# Running the script
if __name__ == "__main__":
    main()