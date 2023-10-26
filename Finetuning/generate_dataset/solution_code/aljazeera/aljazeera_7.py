import csv
from lxml import etree

# HTML Elements with their corresponding XPaths
html_elements = {
    "title": "/html/head/title",
    "close_nav_menu_title": "/html/body/div[1]/div/div[2]/div[1]/div/header/div[3]/button/svg/title",
    "rely_on_us_title": "/html/body/div[3]/div[2]/div/div[1]/div/div[1]/div[2]/h2",
    "nav_menu_title": "/html/body/div[1]/div/div[2]/div[1]/div/header/nav/h2",
    "cookie_policy_link": "/html/body/div[3]/div[2]/div/div[1]/div/div[1]/div[2]/p/a",
    "skip_to_featured_content_link": "/html/body/div[1]/div/div[2]/div[1]/div/header/div[1]/a[1]",
    "hezbollah_article_title": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article[9]/div[2]/div[1]/h3/a/span",
    "asia_nav_link": "/html/body/div[1]/div/div[2]/div[1]/div/header/nav/ul/li[1]/div/ul/li[3]/a/span",
    "middle_east_news_section_title": "/html/body/div[1]/div/div[3]/div/div[1]/div/h1/div",
    "humanitarian_catastrophe_paragraph": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article[3]/div[2]/div[2]/div/p",
    "data_processing_title": "/html/body/div[3]/div[2]/div/div[1]/div/div[1]/div[2]/div/h3",
    "sign_up_for_al_jazeera_title": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div/div/h3",
    "week_in_middle_east_title": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div/div/h4",
    "twitter_icon_title": "/html/body/div[1]/div/div[4]/div[1]/footer/div[2]/div[1]/ul/li[2]/a/svg/title",
    "featured_content_title": "/html/body/div[1]/div/div[3]/div/main/h2",
    "skip_to_content_feed_link": "/html/body/div[1]/div/div[2]/div[1]/div/header/div[1]/a[2]",
    "gaza_attack_article_title": "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[1]/a[1]/span",
    "opinion_nav_link": "/html/body/div[1]/div/div[2]/div[1]/div/header/nav/ul/li[5]/a/span",
    "israeli_air_raids_paragraph": "/html/body/div[1]/div/div[3]/div/main/div/ul/li[1]/article/div[2]/div[2]/div/p",
    "pause_icon_title": "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/button[1]/svg/title",
    "skip_links_title": "/html/body/div[1]/div/div[2]/div[1]/div/header/div[1]/h2",
    "privacy_policy_link": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div/form/div[2]/a",
    "gaza_aid_article_title": "/html/body/div[1]/div/div[3]/div/main/div/ul/li[4]/article/div[2]/div[1]/h3/a/span",
    "article_published_date": "/html/body/div[1]/div/div[3]/div/main/div/ul/li[4]/article/div[2]/footer/div/div/div/div/span[2]",
    "getting_more_aid_to_gaza_paragraph": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article[1]/div[2]/div[2]/div/p",
    "rss_icon_title": "/html/body/div[1]/div/div[4]/div[1]/footer/div[2]/div[1]/ul/li[5]/a/svg/title",
    "content_feed_title": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/h2",
    "al_jazeera_investigative_unit_title": "/html/body/div[1]/div/div[4]/div[1]/footer/div[1]/ul/li[3]/div/ul/li[3]/a/span",
    "al_jazeera_balkans_title": "/html/body/div[1]/div/div[4]/div[1]/footer/div[1]/ul/li[3]/div/ul/li[6]/a/span",
    "beijing_tour_paragraph": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article[6]/div[2]/div[2]/div/p",
    "quotes_icon_title": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article[3]/div[2]/footer/div/div[1]/svg/title",
    "email_confirmation_message": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[2]/div[1]/div/div/form/div[1]/div[3]/span",
    "article_published_date_2": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article[10]/div[2]/footer/div/div/div/div/span[2]",
    "abu_assi_family_paragraph": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article[5]/div[2]/div[2]/div/p",
    "play_icon_title": "/html/body/div[1]/div/div[2]/div[1]/div/header/div[3]/div[2]/div/a/div/svg/title",
    "us_urges_delay_article_title": "/html/body/div[1]/div/div[3]/div/main/div/ul/li[1]/article/div[2]/div[1]/h3/a/span",
    "news_nav_link": "/html/body/div[1]/div/div[2]/div[1]/div/header/nav/ul/li[1]/a/span",
    "us_diplomat_blinken_paragraph": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article[10]/div[2]/div[2]/div/p",
    "close_icon_title": "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/button[2]/svg/title",
    "al_jazeera_copy_right_message": "/html/body/div[1]/div/div[4]/div[1]/footer/div[2]/div[3]/span",
    "article_published_date_3": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article[8]/div[2]/footer/div/div/div/div/span[1]",
    "follow_al_jazeera_title": "/html/body/div[1]/div/div[4]/div[1]/footer/div[2]/div[1]/p",
    "search_icon_title": "/html/body/div[1]/div/div[2]/div[1]/div/header/div[4]/div[3]/button/svg/title",
    "mapping_gaza_neighbourhoods_paragraph": "/html/body/div[1]/div/div[3]/div/div[3]/div/div[1]/section/article[3]/div[2]/div[2]/div/p"
}

# Function to scrape the web page and extract span labels
def scrape_web_page(html_elements):
    tree = etree.parse('downloaded_pages/aljazeera.html', etree.HTMLParser())
    scraped_data = []
    for element, xpath in html_elements.items():
        elements = tree.xpath(xpath)
        for e in elements:
            if e.text:
                scraped_data.append(e.text)
    return scraped_data

# Scrape the web page
scraped_data = scrape_web_page(html_elements)

# Save the data to CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer =