import csv
import os
from pathlib import Path
from selenium import webdriver

# Set the path to chromedriver.exe
chromedriver_path = "path/to/chromedriver.exe"
# Set the path to the downloaded HTML file
html_file_path = "downloaded_pages/quora.html"
# Set the XPaths for the thread titles and descriptions
title_xpath = "/html/body/div[1]/div/h2"
description_xpath = "/html/body/div[1]/div/p"

# Function to scrape the titles and descriptions using Selenium
def scrape_page(url):
    # Configure Selenium to use Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") # Run in headless mode (without opening a browser window)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(chromedriver_path, options=options)

    # Load the local HTML file
    driver.get(url)

    # Find all thread titles and descriptions
    titles = driver.find_elements_by_xpath(title_xpath)
    descriptions = driver.find_elements_by_xpath(description_xpath)

    scraped_data = []

    # Extract the text from the elements and store them as tuples in the scraped_data list
    for i in range(len(titles)):
        title = titles[i].text.strip()
        description = descriptions[i].text.strip()
        scraped_data.append((title, description))

    # Quit the browser driver
    driver.quit()

    return scraped_data

# Function to save the scraped data as a CSV file
def save_as_csv(data):
    csv_file = "scraped_data.csv"
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Description"]) # Write the header row
        writer.writerows(data) # Write the data rows

# Main execution
if __name__ == "__main__":
    # Get the absolute path to the HTML file
    html_file_path = str(Path(html_file_path).resolve())

    # Check if the file exists
    if os.path.exists(html_file_path):
        # Scrape the page
        scraped_data = scrape_page("file://" + html_file_path)

        # Save the data as a CSV file
        save_as_csv(scraped_data)

        print("Scraping completed. The data is saved as 'scraped_data.csv'.")
    else:
        print("The HTML file does not exist. Please provide the correct path.")