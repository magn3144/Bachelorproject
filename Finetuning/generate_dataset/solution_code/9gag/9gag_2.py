import csv
from lxml import etree

def scrape_user_profiles(html_file):
    tree = etree.parse(html_file)
    root = tree.getroot()
    
    profiles = []
    
    profile_elements = root.xpath('//div[@class="user-profile"]')
    for profile_element in profile_elements:
        profile = {'username': '', 'profile_url': ''}
        
        username_element = profile_element.xpath('.//span[@class="username"]')
        if username_element:
            profile['username'] = username_element[0].text.strip()
            
        profile_link_element = profile_element.xpath('.//a[@class="profile-link"]')
        if profile_link_element:
            profile['profile_url'] = profile_link_element[0].get('href')
            
        profiles.append(profile)
        
    return profiles

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['username', 'profile_url'])
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    html_file = 'downloaded_pages/9gag.html'
    scraped_data = scrape_user_profiles(html_file)
    save_to_csv(scraped_data, 'scraped_data.csv')