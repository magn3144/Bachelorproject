import csv
from bs4 import BeautifulSoup

html_file = 'downloaded_pages/homefinder.html'

def parse_html(file):
    with open(file, 'r') as html:
        soup = BeautifulSoup(html, 'html.parser')
        agents = soup.find_all(class_='cobrand-attribution-line1 mt-1')
        brokerages = soup.find_all(class_='cobrand-attribution-label')

        data = []
        for agent, brokerage in zip(agents, brokerages):
            agent_name = agent.text.strip()
            brokerage_name = brokerage.text.strip().split('Courtesy of: ')[-1]
            data.append([agent_name, brokerage_name])

        return data

def save_data(data):
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Agent Name', 'Brokerage Name'])
        writer.writerows(data)

data = parse_html(html_file)
save_data(data)