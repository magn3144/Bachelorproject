import csv
from lxml import etree

# Function to extract titles and links of top-selling games and consoles
def extract_data():
    file_path = 'downloaded_pages/coolshop.html'
    parser = etree.HTMLParser()
    tree = etree.parse(file_path, parser)

    # XPath for top-selling games and consoles
    game_xpath = '//div[@class="product-carousel-title"][contains(text(), "Spil og konsoller")]/following-sibling::div/div[@class="product-carousel-for-user-card"]/a'
    
    games = tree.xpath(game_xpath)

    # Extract titles and links from game elements
    titles = []
    links = []
    for game in games:
        titles.append(game.text)
        links.append(game.get('href'))
    
    return titles, links

# Function to save scraped data as CSV
def save_data(titles, links):
    data = zip(titles, links)

    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Link'])
        writer.writerows(data)

# Main function to execute the script
if __name__ == '__main__':
    titles, links = extract_data()
    save_data(titles, links)