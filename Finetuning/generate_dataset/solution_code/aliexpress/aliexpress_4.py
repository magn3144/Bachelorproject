import csv
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off

# Set up Chrome driver
webdriver_service = Service('path/to/chromedriver')  # Replace with actual path to chromedriver
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Load the local HTML file
html_file = Path('downloaded_pages/aliexpress.html')  # Replace with actual path to the HTML file
driver.get(f'file:///{html_file.absolute()}')

# Find the element using XPath
element_xpath = '/html/body/div[6]/div[1]/div/div[1]/div[8]/a/div'  # Replace with actual XPath
element = driver.find_element(By.XPATH, element_xpath)

# Extract the text from the element
text = element.text

# Save the text as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Scan or click to download'])
    writer.writerow([text])

# Close the browser
driver.quit()