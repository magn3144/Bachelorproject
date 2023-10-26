import csv
from lxml import html


def scrape_weather_conditions(page_content):
    tree = html.fromstring(page_content)
    weather_conditions = []

    month_elements = tree.xpath('/html/body/div/div/div/div[5]/div/main/div[2]/div[3]/div[2]/div[1]/table[1]/tbody/tr/td/span/span')
    for month_element in month_elements:
        weather_conditions.append(month_element.text_content().strip())

    return weather_conditions


def save_to_csv(data, file_name):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Month', 'Weather Conditions'])
        for month, conditions in data:
            writer.writerow([month, conditions])


def main():
    html_file_path = 'downloaded_pages/almanac.html'
    with open(html_file_path, 'r') as html_file:
        content = html_file.read()

    weather_conditions = scrape_weather_conditions(content)
    scraped_data = [(f"Month {i+1}", condition) for i, condition in enumerate(weather_conditions)]
    save_to_csv(scraped_data, 'scraped_data.csv')


if __name__ == "__main__":
    main()