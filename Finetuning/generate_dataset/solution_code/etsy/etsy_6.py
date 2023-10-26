import csv
from selenium import webdriver

# Set up webdriver
driver = webdriver.Chrome()
driver.get("file:///path/to/file/etsy.html")

# Find the element containing the text content of the "Done" button
done_button = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[1]/div/div[3]/div[2]/div/div[3]/button/p")

# Get the text content of the "Done" button
done_text = done_button.text

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([done_text])

# Close the webdriver
driver.quit()