import csv
from bs4 import BeautifulSoup

# HTML file path
html_file = 'downloaded_pages/homefinder.html'

# CSS selectors for apartment listings
address_selector = 'div.addr-component'
agent_selector = 'span.cobrand-attribution-line1'

# Initialize the data list
data = []

# Parse the HTML file
with open(html_file, 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    
    # Find apartment listings
    addresses = soup.select(address_selector)
    agents = soup.select(agent_selector)
    
    # Iterate over the listings and extract the data
    for address, agent in zip(addresses, agents):
        address_text = address.get_text(strip=True)
        agent_text = agent.get_text(strip=True)
        data.append({'Address': address_text, 'Agent': agent_text})

# Save the data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Address', 'Agent'])
    writer.writeheader()
    writer.writerows(data)