import csv
from lxml import etree

def scrape_youtube_comment_likes(local_path, xpaths):
    likes = []

    # Load the HTML file
    with open(local_path, 'r') as html_file:
        html = html_file.read()

    # Parse the HTML
    parser = etree.HTMLParser()
    tree = etree.fromstring(html, parser)

    # Extract the likes using the given xpaths
    for xpath in xpaths:
        likes_element = tree.xpath(xpath)
        if likes_element:
            likes.append(likes_element[0].text.strip())

    # Save the likes as a CSV file
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Likes'])
        writer.writerows(zip(likes))

# Run the scraping function
scrape_youtube_comment_likes('downloaded_pages/youtube-comments.html', [
    '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[107]/ytd-comment-renderer/div[3]/div[2]/div[1]/div[2]/h3/a/span',
    '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[20]/div/ytd-rich-item-renderer[3]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/ytd-video-meta-block/div[1]/div[2]/span[2]',
    '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[55]/div/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/ytd-video-meta-block/div[1]/div[1]/ytd-channel-name/div/tp-yt-paper-tooltip/div',
    '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[35]/div/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/ytd-video-meta-block/div[1]/div[1]/ytd-channel-name/ytd-badge-supported-renderer/div/tp-yt-paper-tooltip/div',
    '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[1]/ytd-engagement-panel-section-list-renderer[2]/div[2]/ytd-structured-description-content-renderer/div/ytd-expandable-video-description-body-renderer/ytd-expander/div/div/yt-attributed-string/span/a[16]',
    '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[32]/ytd-comment-renderer/div[3]/div[2]/div[1]/div[2]/yt-formatted-string/a',
    '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-text-inline-expander/div[2]/ytd-structured-description-content-renderer/div/ytd-video-description-transcript-section-renderer/div[2]/p',
    '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[4]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-compact-video-renderer[3]/div[1]/div/div[1]/a/div/ytd-badge-supported-renderer/div/p',
    '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[4]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-ad-slot-renderer/div/ytd-in-feed-ad-layout-renderer/div/ytd-promoted-sparkles-web-renderer/div[1]/div[2]/div[1]/h3',
    '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-text-inline-expander/div[2]/ytd-structured-description-content-renderer/div/ytd-video-description-infocards-section-renderer/a/div/h3',
    '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[4]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-compact-video-renderer[41]/div[1]/div/div[1]/a/h3/span',
    '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[28]/div/ytd-rich-item-renderer[3]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/ytd-video-meta-block/div[1]/div[2]/span[1]',
    '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[2]/div/ytd-rich-item-renderer[5]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/ytd-video-meta-block/div[1]/div[1]/ytd-channel-name/div/tp-yt-paper-tooltip/div',
    '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[42]/div/ytd-rich-item-renderer[4]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/ytd-video-meta-block/div[1]/div[1]/ytd-channel-name/ytd-badge-supported-renderer/div/tp-yt-paper-tooltip/div',
    '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[1]/ytd-engagement-panel-section-list-renderer[2]/div[2]/ytd-structured-description-content-renderer/div/ytd-expandable-video-description-body-renderer/ytd-expander/div/div/yt-attributed-string/span/a[4]',
    '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-section-renderer[2]/div/ytd-rich-shelf-renderer/div[1]/div[2]/ytd-rich-item-renderer[7]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/ytd-video-meta-block/div[1]/div[1]/ytd-channel-name/div/div/yt-formatted-string/a'
    ])