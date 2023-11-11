import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Run Chrome in headless mode

# Set up Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Load the HTML page
driver.get("file:///path/to/downloaded_pages/booking.html")

# Set up empty list to store scraped data
scraped_data = []

# Find all facility names
facility_names = driver.find_elements(By.XPATH, "//h4[@class='abf093bdfe e8f7c070a7']")
# Find all icons for each property
icons = driver.find_elements(By.XPATH, "//div[@class='a53cbfa6de e7c28a2436']")

# Loop through each facility and corresponding icon
for name, icon in zip(facility_names, icons):
    facility = {}
    facility['name'] = name.text
    facility['icon'] = icon.text
    scraped_data.append(facility)

# Close the Chrome driver
driver.quit()

# Save scraped data as CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'icon']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for facility in scraped_data:
        writer.writerow(facility)