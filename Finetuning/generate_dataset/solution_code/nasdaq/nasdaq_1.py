import csv
from pathlib import Path
from selenium import webdriver

# Set the path to the downloaded HTML file
html_path = Path("downloaded_pages/nasdaq.html")

# Set the XPath for the clickable links
link_xpath = '//a'

# Initialize the web driver
driver = webdriver.Chrome()

# Load the local HTML file
driver.get(f'file://{html_path.absolute()}')

# Find all the clickable links on the page
links = driver.find_elements_by_xpath(link_xpath)

# Extract the link texts
link_texts = [link.text.strip() for link in links]

# Save the link texts in a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Link Text'])
    writer.writerows([[link] for link in link_texts])

# Close the web driver
driver.quit()