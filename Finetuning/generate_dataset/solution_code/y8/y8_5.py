import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up the Chrome driver options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the Chrome driver with the configured options
driver = webdriver.Chrome(options=chrome_options)

# Load the local HTML file
driver.get("file:///path/to/downloaded_pages/y8.html")

# Define the XPaths for the target element
xpath = "/html/body/footer/div/div/div[2]/ul/li[5]/a"

# Find the target element using its XPath
target_element = driver.find_element(By.XPATH, xpath)

# Extract the text from the target element
text = target_element.text.strip()

# Save the extracted text to a CSV file
with open("scraped_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([text])

# Close the Chrome driver
driver.quit()