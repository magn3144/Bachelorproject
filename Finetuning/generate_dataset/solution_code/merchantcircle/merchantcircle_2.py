import csv
from bs4 import BeautifulSoup

# Define the target HTML file path
html_file_path = "downloaded_pages/merchantcircle.html"

# Create a function to scrape the text of all url org tags
def scrape_url_org_tags(html_file_path):
    with open(html_file_path, "r") as file:
        soup = BeautifulSoup(file, "html.parser")
        url_org_tags = soup.find_all("a", class_="url org")
        url_org_texts = [tag.get_text(strip=True) for tag in url_org_tags]
        return url_org_texts

# Scrape the text of all url org tags
url_org_texts = scrape_url_org_tags(html_file_path)

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["URL"])
    writer.writerows([text] for text in url_org_texts)