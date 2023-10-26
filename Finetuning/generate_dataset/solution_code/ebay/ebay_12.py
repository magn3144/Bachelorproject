import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set the path to the chromedriver executable
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_driver = "path/to/chromedriver"  # Replace with the actual path to chromedriver

# Instantiate the webdriver
driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)

# Load the local HTML file
driver.get("file:///path/to/downloaded_pages/ebay.html")

# Find the element using XPath
element_xpath = "/html/body/div[6]/footer/h2"
element = driver.find_element(By.XPATH, element_xpath)

# Get the text from the element
text = element.text

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([text])

# Close the webdriver
driver.quit()