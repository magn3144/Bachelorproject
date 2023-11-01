import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Load the HTML file
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('file:///path/to/downloaded_pages/ældresagen.html')

# Find the housing options
housing_types = driver.find_elements(By.XPATH, "//span[contains(text(), 'Boligtyper til')]")

# Extract the text from the housing options
housing_options = [housing.text for housing in housing_types]

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Housing Options'])
    writer.writerows(zip(housing_options))

driver.quit()