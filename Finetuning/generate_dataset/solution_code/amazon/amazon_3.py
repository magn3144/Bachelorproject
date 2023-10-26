import csv
from lxml import html

def scrape_shipping_rates():
    # Load the HTML file
    with open('downloaded_pages/amazon.html', 'r') as file:
        page_content = file.read()
    
    # Create the CSV file
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Shipping Rate', 'Policy'])
        
        # Parse the HTML
        tree = html.fromstring(page_content)
        
        # Scrape the shipping rate and policy information
        shipping_rate_elements = tree.xpath('//a[contains(text(), "Shipping Rates")]')
        policy_elements = tree.xpath('//a[contains(text(), "Policies")]')
        
        # Write the scraped data to the CSV file
        for shipping_element, policy_element in zip(shipping_rate_elements, policy_elements):
            shipping_rate = shipping_element.text
            policy = policy_element.text
            writer.writerow([shipping_rate, policy])

# Scrape the shipping rates and policies
scrape_shipping_rates()