# Script:

```python
import csv
from lxml import html

# Read HTML file
with open('downloaded_pages/coursera.html', 'r') as file:
    html_content = file.read()

# Create XPath dictionary
xpath_dict = {
    'business_description': '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[1]/div/div/div[2]/ul/li[2]/button/span[2]',
    'random_element_1': '/html/body/div[2]/div/div/main/div[2]/div/div/div/div/div[2]/div[3]/div[2]/div[8]/a/span[1]',
    'specialization_duration': '/html/body/div[2]/div/div/main/div[2]/div/div/div/div/div[2]/ul/li[4]/div/div/div/div/div/div[2]/div[3]/div[4]/p',
    'certificate_programs_title': '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[5]/div/section/div/div[2]/div[1]/div[2]/div/p',
    'data_analytics_master': '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[5]/div/section/div/div[2]/div[1]/div[1]/div/ul/li[2]/div/a/div/div/div[2]',
    'public_health_master': '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[10]/div/section/div/div[2]/div[1]/div/div/ul/li[1]/div/a/div/div/div[2]',
    'guided_projects': '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[14]/div/section/div/div[2]/div[2]/div[1]/ul/li[3]/div/a',
    'design': '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[14]/div/section/div/div[2]/div[2]/div[2]/ul/li[1]/div/a',
    'hidden_pages_title': '/html/body/div[2]/div/div/main/div[2]/div/div/div/div/div[2]/div[4]/div/nav/ul/li[7]/div/svg/title',
    'online_degrees_title': '/html/body/div[2]/div/div/main/div[1]/div/div/section/div/h2',
    'pg_machine_learning': '/html/body/div[2]/div/div/main/div[1]/div/div/section/div/div[1]/div/div/div[19]/div/div/div/a/div/div[2]/h3',
    'ibm_ai_engineering': '/html/body/div[2]/div/div/main/div[1]/div/div/section/div/div[1]/div/div/div[11]/div/div/div/a/div/div[2]/h3',
    'copyright': '/html/body/div[2]/div/div/div/footer/div/div/div/div[9]/div/div[1]/span',
    'self_paced': '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[12]/div/section/div/div[2]/div[1]/div[2]/div/ul/li[2]/div/a/div/div/div[2]/span/span',
    'beginner_specialization': '/html/body/div[2]/div/div/main/div[2]/div/div/div/div/div[2]/ul/li[1]/div/div/div/div/div/div[2]/div[3]/div[3]/p',
    'iit_roorkee': '/html/body/div[2]/div/div/main/div[1]/div/div/section/div/div[1]/div/div/div[9]/div/div/div/a/div/div[2]/p',
    'liberal_studies_ba': '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[6]/div/section/div/div[2]/div[1]/div[1]/div/ul/li[4]/div/a/div/div/div[2]',
    'northeastern_university': '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[8]/div/section/div/div[2]/div[1]/div[1]/div/ul/li[6]/div/a/div/div/div[1]',
    'mastertrack_certificates': '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[2]/div/section/div/div[2]/div[5]/ul/li[2]/a',
    'view_all_degrees': '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[5]/div/section/div/div[2]/div[1]/div[1]/div/ul/li[7]/a',
    'close_button': '/html/body/div[2]/div/div/span/div[1]/header/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div/nav/div/div/div[2]/div[6]/div/section/div/button/span/svg/title',
    'related_searches_title': '/html/body/div[2]/div/div/main/div[2]/div/div/div/div/div[2]/div[3]/div[1]/h2',
    'pg_machine_learning_again': '/html/body/div[2]/div/div/main/div[1]/div/div/section/div/div[1]/div/div/div[9]/div/div/div/a/div/div[2]/h3',
    'deep_learning': '/html/body/div[2]/div/div/main/div[2]/div/div/div/div/div[2]/ul/li[4]/div/div/div/div/div/div[2]/div[1]/div[2]/a/h3'
}

# Scrape data
data = {
    'business_description': html.fromstring(html_content).xpath(xpath_dict['business_description'])[0].text.strip(),
    'random_element_1': html.fromstring(html_content).xpath(xpath_dict['random_element_1'])[0].text.strip(),
    'specialization_duration': html.fromstring(html_content).xpath(xpath_dict['specialization_duration'])[0].text.strip(),
    'certificate_programs_title': html.fromstring(html_content).xpath(xpath_dict['certificate_programs_title'])[0].text.strip(),
    'data_analytics_master': html.fromstring(html_content).xpath(xpath_dict['data_analytics_master'])[0].text.strip(),
    'public_health_master': html.fromstring(html_content).xpath(xpath_dict['public_health_master'])[0].text.strip(),
    'guided_projects': html.fromstring(html_content).xpath(xpath_dict['guided_projects'])[0].text.strip(),
    'design': html.fromstring(html_content).xpath(xpath_dict['design'])[0].text.strip(),
    'hidden_pages_title': html.fromstring(html_content).xpath(xpath_dict['hidden_pages_title'])[0].text.strip(),
    'online_degrees_title': html.fromstring(html_content).xpath(xpath_dict['online_degrees_title'])[0].text.strip(),
    'pg_machine_learning': html.fromstring(html_content).xpath(xpath_dict['pg_machine_learning'])[0].text.strip(),
    'ibm_ai_engineering': html.fromstring(html_content).