import csv
from bs4 import BeautifulSoup

# Target HTML file
html_file = 'downloaded_pages/youtube-comments.html'

# HTML elements
elements = [
    {
        'element': 'span',
        'attributes': {'class': 'style-scope ytd-comment-renderer style-scope ytd-comment-renderer'},
        'xpath': '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[107]/ytd-comment-renderer/div[3]/div[2]/div[1]/div[2]/h3/a/span'
    },
    {
        'element': 'span',
        'attributes': {'class': 'inline-metadata-item style-scope ytd-video-meta-block'},
        'xpath': '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[20]/div/ytd-rich-item-renderer[3]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/ytd-video-meta-block/div[1]/div[2]/span[2]'
    },
    {
        'element': 'div',
        'attributes': {'class': 'hidden style-scope tp-yt-paper-tooltip', 'id': 'tooltip'},
        'xpath': '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[55]/div/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/ytd-video-meta-block/div[1]/div[1]/ytd-channel-name/div/tp-yt-paper-tooltip/div'
    },
    {
        'element': 'div',
        'attributes': {'class': 'hidden style-scope tp-yt-paper-tooltip', 'id': 'tooltip'},
        'xpath': '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[35]/div/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/ytd-video-meta-block/div[1]/div[1]/ytd-channel-name/ytd-badge-supported-renderer/div/tp-yt-paper-tooltip/div'
    },
    {
        'element': 'a',
        'attributes': {'class': 'yt-core-attributed-string__link yt-core-attributed-string__link--display-type yt-core-attributed-string__link--call-to-action-color'},
        'xpath': '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[1]/ytd-engagement-panel-section-list-renderer[2]/div[2]/ytd-structured-description-content-renderer/div/ytd-expandable-video-description-body-renderer/ytd-expander/div/div/yt-attributed-string/span/a[16]'
    },
    {
        'element': 'a',
        'attributes': {'class': 'yt-simple-endpoint style-scope yt-formatted-string'},
        'xpath': '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[32]/ytd-comment-renderer/div[3]/div[2]/div[1]/div[2]/yt-formatted-string/a'
    },
    {
        'element': 'p',
        'attributes': {'class': 'style-scope ytd-video-description-transcript-section-renderer', 'id': 'sub-header-text'},
        'xpath': '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-text-inline-expander/div[2]/ytd-structured-description-content-renderer/div/ytd-video-description-transcript-section-renderer/div[2]/p'
    },
    {
        'element': 'p',
        'attributes': {'class': 'style-scope ytd-badge-supported-renderer'},
        'xpath': '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[4]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-compact-video-renderer[3]/div[1]/div/div[1]/a/div/ytd-badge-supported-renderer/div/p'
    },
    {
        'element': 'h3',
        'attributes': {'class': 'style-scope ytd-promoted-sparkles-web-renderer yt-simple-endpoint', 'id': 'title'},
        'xpath': '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[4]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-ad-slot-renderer/div/ytd-in-feed-ad-layout-renderer/div/ytd-promoted-sparkles-web-renderer/div[1]/div[2]/div[1]/h3'
    },
    {
        'element': 'h3',
        'attributes': {'class': 'style-scope ytd-video-description-infocards-section-renderer', 'id': 'title'},
        'xpath': '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-text-inline-expander/div[2]/ytd-structured-description-content-renderer/div/ytd-video-description-infocards-section-renderer/a/div/h3'
    },
    {
        'element': 'span',
        'attributes': {'class': 'style-scope ytd-compact-video-renderer style-scope ytd-compact-video-renderer', 'id': 'video-title'},
        'xpath': '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[4]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-compact-video-renderer[41]/div[1]/div/div[1]/a/h3/span'
    },
    {
        'element': 'span',
        'attributes': {'class': 'inline-metadata-item style-scope ytd-video-meta-block'},
        'xpath': '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[28]/div/ytd-rich-item-renderer[3]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/ytd-video-meta-block/div[1]/div[2]/span[1]'
    },
    {
        'element': 'div',
        'attributes': {'class': 'hidden style-scope tp-yt-paper-tooltip', 'id': 'tooltip'},
        'xpath': '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[2]/div/ytd-rich-item-renderer[5]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/ytd-video-meta-block/div[1]/div[1]/ytd-channel-name/div/tp-yt-paper-tooltip/div'
    },
    {
        'element': 'div',
        'attributes': {'class': 'hidden style-scope tp-yt-paper-tooltip', 'id': 'tooltip'},
        'xpath': '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[42]/div/ytd-rich-item-renderer[4]/div/ytd-rich-grid-media/div[1]/div[3]/div[1]/ytd-video-meta-block/div[1]/div[1]/ytd-channel-name/ytd-badge-supported-renderer/div/tp-yt-paper-tooltip/div'
    },
    {
        'element': 'a',
        'attributes': {'class': 'yt-core-attributed-string__link yt-core-attributed-string__link--