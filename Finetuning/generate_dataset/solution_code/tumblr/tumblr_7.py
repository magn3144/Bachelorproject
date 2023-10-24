import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the path to the downloaded HTML file
html_path = "downloaded_pages/tumblr.html"

# Set up the Chrome driver
driver = webdriver.Chrome("chromedriver")

# Load the HTML file
driver.get(f"file:///{html_path}")

# Find all the message entries on the page
message_entries = driver.find_elements(By.XPATH, "//div[contains(@class, 'rZlUD W45iW')]")

# Extract the text from the message entries
messages = [entry.text for entry in message_entries]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Message'])
    for message in messages:
        writer.writerow([message])

# Close the driver
driver.quit()