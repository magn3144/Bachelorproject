import csv
from bs4 import BeautifulSoup

# Read the HTML file
with open("downloaded_pages/bleacherreport.html", "r") as file:
    html_content = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the providers
providers = soup.find_all("span", class_="provider")

# Extract the text from each provider
provider_list = [provider.get_text(strip=True) for provider in providers]

# Write the data to a CSV file
with open("scraped_data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Provider"])
    writer.writerows(zip(provider_list))