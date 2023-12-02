import csv
import lxml.html as html

def main():
    dom = html.parse('downloaded_pages/imdb.html')

    with open('scraped_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Movie Title', 'User Rating'])

        for i in range(1, 251):
            title_path = f'/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[{i}]/div[2]/div/div/div[1]/a/h3'
            rating_path = f'/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[{i}]/div[2]/div/div/span/div/span/span'

            title_element = dom.xpath(title_path)
            rating_element = dom.xpath(rating_path)

            if title_element and rating_element:
                movie_title = title_element[0].text_content()
                user_rating = rating_element[0].text_content().strip()[1:-1] 

                writer.writerow([movie_title, user_rating])

if __name__=='__main__':
    main()