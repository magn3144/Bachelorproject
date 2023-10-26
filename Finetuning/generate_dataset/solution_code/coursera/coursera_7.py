# Script to solve the task of scraping names of guided projects and saving them as a CSV file

import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set up the Selenium webdriver
s = Service("path/to/chromedriver")  # Replace with the path to your chromedriver executable
driver = webdriver.Chrome(service=s)

# Load the local HTML file
driver.get("file:///path/to/downloaded_pages/coursera.html")  # Replace with the path to the downloaded HTML file

# Find the guided project elements using XPath
guided_project_elements = driver.find_elements(By.XPATH, "//a[contains(@class, 'rc-SimpleGoalItem')]")

# Extract the names from the guided project elements and store them in a list
guided_project_names = [element.text for element in guided_project_elements]

# Save the extracted names as a CSV file
with open("scraped_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Guided Project Name"])  # Write the header row
    writer.writerows([[name] for name in guided_project_names])

# Quit the webdriver
driver.quit()