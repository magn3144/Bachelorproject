import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set Chrome options to run in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Set the path to the downloaded HTML file
html_file_path = "downloaded_pages/9gag.html"

# Set the XPaths of the logo link and latest post URLs
logo_xpath = "/html/body/div[1]/header/div/a[2]"
latest_post_xpath = "/html/body/span"

# Function to scrape the latest post URLs
def scrape_latest_posts():
    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Load the local HTML file
    driver.get(f"file://{html_file_path}")
    
    # Find the logo link element
    logo_link = driver.find_element(By.XPATH, logo_xpath)
    
    # Get the href attribute of the logo link
    logo_link_url = logo_link.get_attribute("href")
    
    # Find the latest post element
    latest_post_element = driver.find_element(By.XPATH, latest_post_xpath)
    
    # Get the text of the latest post element
    latest_post_text = latest_post_element.text
    
    # Close the Chrome driver
    driver.quit()
    
    # Split the latest post text by commas to get the URLs
    latest_post_urls = latest_post_text.split(",")
    
    return logo_link_url, latest_post_urls

# Function to save the scraped data as a CSV file
def save_data_to_csv(logo_url, post_urls):
    # Create a list of dictionaries for the data
    data = [{"Logo URL": logo_url, "Post URL": post_url} for post_url in post_urls]
    
    # Set the fieldnames for the CSV file
    fieldnames = ["Logo URL", "Post URL"]
    
    # Write the data to the CSV file
    with open("scraped_data.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Main function to run the script
def main():
    # Scrape the latest posts
    logo_url, post_urls = scrape_latest_posts()
    
    # Save the scraped data as a CSV file
    save_data_to_csv(logo_url, post_urls)

# Run the main function
if __name__ == "__main__":
    main()