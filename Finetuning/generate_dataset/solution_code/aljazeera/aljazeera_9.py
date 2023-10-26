import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Set up Chrome driver
driver = webdriver.Chrome(chrome_options=chrome_options)

# Load the local HTML file
driver.get("file:///path/to/downloaded_pages/aljazeera.html")

# Find the footer element
footer_element = driver.find_element(By.XPATH, "//footer")

# Extract the text from the footer element
footer_text = footer_element.text

# Close the Chrome driver
driver.quit()

# Save the scraped data to CSV
data = [["Scraped Data"],
        [footer_text]]

with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)