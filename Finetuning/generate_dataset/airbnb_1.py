import csv
import bs4


def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

with open('downloaded_pages/airbnb.html', 'r') as f:
    content = f.read()

soup = bs4.BeautifulSoup(content, 'html.parser')

# Find button element with the text "Show more"
show_more_button_class = soup.find('button', text='Show more')['class']
write_to_csv([show_more_button_class], 'scraped_data.csv')