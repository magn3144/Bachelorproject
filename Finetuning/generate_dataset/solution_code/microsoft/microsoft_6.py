import csv
from selenium import webdriver

# Define the local path to the HTML file
html_file = "downloaded_pages/microsoft.html"

# Open the HTML file using Selenium WebDriver
driver = webdriver.Chrome()
driver.get("file:///" + html_file)

# Create a list to store the names of global categories
global_categories = []

# Find all elements with class "c-uhf-sronly" (global category names)
categories_elements = driver.find_elements_by_class_name("c-uhf-sronly")

# Extract the text from the elements and add them to the list
for element in categories_elements:
    global_categories.append(element.text)

# Close the WebDriver
driver.quit()

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Global Categories"])
    writer.writerows(zip(global_categories))