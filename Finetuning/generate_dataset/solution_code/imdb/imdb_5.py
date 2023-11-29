import csv
import lxml.html

def scrape_html(file_path):
    tree = lxml.html.parse(file_path)
    root = tree.getroot()
    
    movies = root.xpath('//div[@class="ipc-title__text"]/a/h3')
    ratings = root.xpath('//span[@class="ipc-rating-star--voteCount"]')

    data = []
    for movie, rating in zip(movies, ratings):
        data.append([movie.text, rating.text.strip()])

    return data

def save_to_csv(data, file_path):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Title", "Ratings count"])
        writer.writerows(data)

if __name__ == "__main__":
    data = scrape_html('downloaded_pages/imdb.html')
    save_to_csv(data, 'scraped_data.csv')