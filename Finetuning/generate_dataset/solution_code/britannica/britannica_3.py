import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Specify the path to the chromedriver executable
webdriver_service = Service('path/to/chromedriver')

# Launch the Chrome browser using the chromedriver
driver = webdriver.Chrome(service=webdriver_service)

# Load the local HTML file
driver.get("file:///path/to/downloaded_pages/britannica.html")

# Find the hidden elements in the header using XPath
hidden_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'd-none') or contains(@class, 'hidden')]")

# Create a CSV file to save the scraped data
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Text'])

    # Save the hidden elements in the CSV file
    for element in hidden_elements:
        writer.writerow([element.text])

# Close the browser
driver.quit()