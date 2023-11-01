import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(options=chrome_options)

# Load the webpage
driver.get("file:///path/to/downloaded_pages/9gag.html")

# Scrape post titles
post_titles = driver.find_elements(By.XPATH, "//article//h2[@class='badge-item-title']")

# Save scraped data as CSV
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Post Title"])
    for title in post_titles:
        writer.writerow([title.text])

# Close the browser
driver.quit()