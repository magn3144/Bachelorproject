import csv
from bs4 import BeautifulSoup

# Function to extract the target data from HTML file
def scrape_data(html_file):
    with open(html_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        
        # Find all <span> elements with class "rate-thankyouText"
        target_elements = soup.find_all('span', class_='rate-thankyouText')
        
        # Extract the text content from target elements
        target_data = [element.get_text().strip() for element in target_elements]
        
        return target_data

# Run the function to scrape the data
scraped_data = scrape_data('downloaded_pages/census.html')

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Thank You Text'])
    writer.writerows(zip(scraped_data))