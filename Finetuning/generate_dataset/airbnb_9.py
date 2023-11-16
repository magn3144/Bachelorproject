import pandas as pd
from lxml import html

# Reading the content of html file
with open("downloaded_pages/airbnb.html", "r") as file:
    page_content = file.read()

tree = html.fromstring(page_content)

# Getting the location elements 
location_elements = tree.xpath('//div[@class="t1jojoys dir dir-ltr"]')

# Getting the 'Guest favorite' elements
guest_fav_elements = tree.xpath('//div[@class="t1qa5xaj dir dir-ltr"]')

locations = [element.text for element in location_elements]
guest_favs = ['Yes' if element.text == 'Guest favorite' else 'No' for element in guest_fav_elements]

# Creating DataFrame 
data_dict = {'Location': locations[:min(len(locations), len(guest_favs))], 
             'Guest_Favorite': guest_favs[:min(len(locations), len(guest_favs))]}
df = pd.DataFrame(data_dict)

# Saving DataFrame to csv file
df.to_csv('scraped_data.csv', index=False)