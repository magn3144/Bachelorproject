import csv
from bs4 import BeautifulSoup

# Open the HTML file and read its contents
with open('downloaded_pages/homefinder.html', 'r') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all the elements containing the agent names and agencies
agent_elements = soup.find_all('span', class_='cobrand-attribution-line1 mt-1')

# Extract the agent names and agencies
agent_data = []
for element in agent_elements:
    agent_name = element.text.strip()
    agency = element.next_sibling.string.strip()
    agent_data.append([agent_name, agency])

# Save the scraped data as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(agent_data)