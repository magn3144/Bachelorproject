import csv
from lxml import etree

# Define the HTML elements and XPaths
elements = {
    'plays_count': '/html/body/div[1]/div[5]/div[2]/ul/li[11]/a/div[2]/div[3]',
    'tag': '/html/body/div[1]/div[1]/div/div[2]/div/div/ul/li[4]/a/div',
    'username': '/html/body/nav/div[1]/div[2]/div[5]/div[2]/div[2]/div/div[1]/span[1]',
    'percentage': '/html/body/div[1]/div[5]/div[2]/ul/li[8]/a/div[2]/div[2]/span',
    'multiplayer_games': '/html/body/div[4]/div/div/div[2]/p[2]/a[3]',
    'browse_games_studios': '/html/body/footer/div/div/div[2]/ul/li[5]/a',
    'all_categories': '/html/body/div[1]/div[1]/div/div[1]/div/ul/li[13]',
    'html5': '/html/body/div[1]/div[5]/div[2]/ul/li[61]/a/div[2]/div[1]/p',
    'game_title': '/html/body/div[1]/div[5]/div[2]/ul/li[11]/a/div[2]/p',
    'pre-content_title': '/html/body/div[3]/div/h1',
    'pre-content_description': '/html/body/div[3]/div/h2',
    'pre-content_title-red': '/html/body/div[4]/div/div/div[1]/h2',
    'new_games_categories_rise': '/html/body/div[4]/div/div/div[2]/h3[1]',
    'extensive_game_network': '/html/body/div[4]/div/div/div[3]/h3[2]',
    'flag_country': '/html/body/nav/div[1]/div[2]/div[6]/div/ul/li[9]/a/div[1]',
    'sub_title': '/html/body/nav/div[1]/div[2]/div[3]/span',
    'flash_games_archive': '/html/body/div[4]/div/div/div[3]/p[2]/a[2]',
    'two_player': '/html/body/div[1]/div[2]/div/div/div/div[2]/ul/li[15]/a',
    'desktop_only': '/html/body/div[1]/div[5]/div[2]/ul/li[56]/div/p',
    'game_categories': '/html/body/div[4]/div/div/div[2]/h2',
    'evolution_of_browser_games': '/html/body/div[4]/div/div/div[1]/h3[3]',
    'plays_count2': '/html/body/div[1]/div[5]/div[2]/ul/li[16]/a/div[2]/div[3]',
    'flag_language': '/html/body/nav/div[1]/div[2]/div[6]/div/ul/li[18]/a/div[2]',
    'new_item_icon': '/html/body/div[1]/div[5]/div[2]/ul/li[24]/a/span',
    'played_games': '/html/body/nav/div[1]/div[2]/div[5]/div[2]/div[2]/div/ul/li[4]/a',
    'edit_profile': '/html/body/nav/div[1]/div[2]/div[5]/div[2]/div[2]/div/ul/li[2]/a',
    'tooltip_description': '/html/body/div[1]/div[5]/div[2]/ul/li[24]/a/div[4]/p',
    'game_title2': '/html/body/div[1]/div[5]/div[2]/ul/li[15]/a/div[2]/p',
    'technologies': '/html/body/div[4]/div/div/div[3]/h2',
    'connect_with_player_community': '/html/body/div[4]/div/div/div[3]/h3[3]',
    'best_games': '/html/body/nav/div[1]/div[2]/div[2]/div/ul/li[3]/a/div[1]',
    'flag_language2': '/html/body/nav/div[1]/div[2]/div[6]/div/ul/li[15]/a/div[2]',
    'new_item_icon2': '/html/body/div[1]/div[5]/div[2]/ul/li[14]/a/span',
    'new_games_released_hourly': '/html/body/div[4]/div/div/div[1]/p[2]/a[2]',
    'cooking': '/html/body/div[1]/div[2]/div/div/div/div[2]/ul/li[11]/a',
    'html5_games': '/html/body/div[1]/div[5]/div[2]/ul/li[47]/a/div[2]/div[1]/p',
    'game_title3': '/html/body/div[1]/div[5]/div[2]/ul/li[3]/a/div[2]/p',
    'discover_multiplayer_gaming': '/html/body/div[4]/div/div/div[2]/h3[2]',
    'plays_count3': '/html/body/div[1]/div[5]/div[2]/ul/li[50]/a/div[2]/div[3]',
    'flag_country2': '/html/body/nav/div[1]/div[2]/div[6]/ul/li/a/div[1]',
    'management_sim': '/html/body/div[1]/div[1]/div/div[1]/div/ul/li[6]/a/span',
    'html5_boost_legacy': '/html/body/div[4]/div/div/div[3]/p[2]/a[1]',
    'horror': '/html/body/div[1]/div[2]/div/div/div/div[2]/ul/li[12]/a',
    'tooltip_description2': '/html/body/div[1]/div[5]/div[2]/ul/li[34]/a/div[4]/p',
    'game_title4': '/html/body/div[1]/div[5]/div[2]/ul/li[22]/a/div[2]/p',
    'y8_ultimate_gaming': '/html/body/div[4]/div/div/div[1]/h3[2]',
    'plays_count4': '/html/body/div[1]/div[5]/div[2]/ul/li[4]/a/div[2]/div[3]'
}

# Parse the HTML file
tree = etree.parse('downloaded_pages/y8.html')

# Extract the game title using the XPath
game_title = tree.xpath(elements['game_title'])[0].text.strip()

# Save the game title as a CSV file
with open('scraped_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Game Title'])
    writer.writerow([game_title])