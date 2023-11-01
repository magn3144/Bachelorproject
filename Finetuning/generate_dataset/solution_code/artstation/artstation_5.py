import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the path to the downloaded HTML file
html_path = "downloaded_pages/artstation.html"

# Set the category and website details
category = "Digital Websites"
website = "artstation"

# Set the XPath of the form labels
form_label_xpath = "//label[@class='form-label bs-control-label']"

# Initialize the web driver
driver = webdriver.Chrome()

# Load the local HTML file
driver.get("file://" + html_path)

# Find all form labels with the given XPath
form_labels = driver.find_elements(By.XPATH, form_label_xpath)

# Scrape the text from the form labels
scraped_data = [label.text for label in form_labels]

# Close the driver
driver.quit()

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Category", "Website", "Form Label"])
    for label in scraped_data:
        writer.writerow([category, website, label])