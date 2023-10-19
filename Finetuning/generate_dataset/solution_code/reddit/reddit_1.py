import csv
from bs4 import BeautifulSoup

html_file = 'downloaded_pages/reddit.com.html'

def extract_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    posts = []

    for post in soup.find_all('div', {'data-testid': 'post-container'}):
        title = post.find('h3', {'class': '_eYtD2XCVieq6emjKBH3m'}).text
        author = post.find('a', {'class': '_2tbHP6ZydRpjI44J3syuqC'}).text
        upvotes = post.find('div', {'class': '_1rZYMD_4xY3gRcSS3p8ODO'}).text

        posts.append({'Title': title, 'Author': author, 'Upvotes': upvotes})

    return posts

def save_to_csv(data):
    with open('reddit_posts.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Title', 'Author', 'Upvotes'])
        writer.writeheader()
        writer.writerows(data)

with open(html_file, 'r', encoding='utf-8') as file:
    html_data = file.read()

posts_data = extract_data(html_data)
save_to_csv(posts_data)