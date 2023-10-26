import csv
from lxml import etree

# Define the XPaths and their corresponding text
xpaths = [
    ("/html/body/div[3]/div[4]/h1/span", "Registered sex offenders in Abbeville, Alabama"),
    ("/html/body/div[3]/div[4]/div[4]/div/span", "13465 State Highway 95 N"),
    ("/html/body/div[3]/div[4]/div[14]/div/a[2]", "Based on this official offender page"),
    ("/html/body/div[1]/div/div/div[2]/ul/li[6]/ul/table/tbody/tr[2]/td[4]/a", "HI"),
    ("/html/body/ol[1]/li[6]", "Registered sex offenders in Abbeville, Alabama"),
    ("/html/body/div[3]/div[4]/div[2]/div/div[1]/div[1]/ul/li[1]", "OSM Map"),
    ("/html/body/div[3]/div[4]/div[2]/div/h3", "Your use of this information constitutes agreement"),
    ("/html/body/div[3]/div[4]/p[1]", "No representation is made that the persons listed"),
    ("/html/body/div[3]/div[4]/div[2]/div/div[1]/div[1]/span", "Note: 5 addresses could not be displayed on map."),
    ("/html/body/div[3]/div[4]/div[4]/strong/span", "Arthur Chandler Duncan"),
    ("/html/body/div[3]/div[4]/div[12]/div/a[2]", "Based on this official offender page"),
    ("/html/body/div[1]/div/div/div[2]/ul/li[10]/ul/table/tbody/tr[1]/td[4]/a", "DC"),
    ("/html/body/ol[2]/li[6]", "Registered sex offenders in Abbeville, Alabama"),
    ("/html/body/div[3]/div[4]/div[2]/div/div[1]/div[3]/ul/li[1]", "OSM Map"),
    ("/html/body/div[3]/div[4]/div[2]/div/p[2]", "THE INFORMATION PROVIDED ON THIS SITE IS PROVIDED"),
    ("/html/body/div[3]/div[4]/div[11]/strong/span", "George Mark Danzy"),
    ("/html/body/ol[1]/li[5]/a", "Registered sex offenders in Alabama"),
    ("/html/body/div[1]/div/div/div[2]/ul/li[4]/ul/table/tbody/tr[6]/td[4]/a", "SC"),
    ("/html/body/div[3]/div[4]/div[2]/div/div[1]/div[1]/ul/li[2]", "Google Map"),
    ("/html/body/div[3]/div[4]/div[22]/div/span", "1489 County Road 84"),
    ("/html/body/div[3]/div[4]/div[17]/div/a[2]", "Based on this official offender page"),
    ("/html/body/div[1]/div/div/div[2]/ul/li[8]/ul/table/tbody/tr[4]/td[3]/a", "NM"),
    ("/html/body/div[3]/div[4]/div[2]/div/div[1]/div[2]/ul/li[1]", "OSM Map"),
    ("/html/body/div[3]/div[4]/div[7]/div/span", "290 Singletary Rd"),
    ("/html/body/div[1]/div/div/div[2]/ul/li[12]/ul/li[8]/a", "Tourist Attractions Articles"),
    ("/html/body/div[1]/div/div/div[2]/ul/li[12]/ul/li[1]/ul/table/tbody/tr[6]/td[5]/a", "RI"),
    ("/html/body/div[3]/div[4]/div[2]/div/div[1]/div[2]/ul/li[3]", "Bing Map"),
    ("/html/body/div[3]/div[4]/div[23]/strong/span", "Robert Dewayne Deese"),
    ("/html/body/div[3]/div[4]/div[21]/div/a[2]", "Based on this official offender page"),
    ("/html/body/div[1]/div/div/div[2]/ul/li[6]/ul/table/tbody/tr[6]/td[2]/a", "PA"),
    ("/html/body/div[3]/div[4]/div[2]/div/div[1]/div[3]/ul/li[2]", "Google Map"),
    ("/html/body/div[3]/div[4]/div[5]/strong/span", "Bennie Joe Lacy"),
    ("/html/body/div[3]/div[4]/div[24]/div/a[2]", "Based on this official offender page"),
    ("/html/body/div[1]/div/div/div[2]/ul/li[8]/ul/table/tbody/tr[4]/td[1]/a", "NE"),
    ("/html/body/div[3]/div[4]/div[2]/div/div[1]/div[3]/ul/li[3]", "Bing Map"),
    ("/html/body/div[3]/div[4]/div[8]/div/span", "266 Co Rd 210"),
    ("/html/body/div[3]/div[4]/div[30]/div/a", "Based on this official offender page"),
    ("/html/body/div[1]/div/div/div[2]/ul/li[12]/ul/li[4]/ul/table/tbody/tr[1]/td[4]/a", "NB"),
    ("/html/body/div[3]/div[4]/div[2]/div/div[1]/div[2]/ul/li[2]", "Google Map"),
    ("/html/body/div[3]/div[4]/div[13]/div/span", "6307 County Road 57 S"),
    ("/html/body/div[3]/div[4]/div[2]/div/div[1]/div[1]/div/div[3]/div[4]/div/a[3]", "OpenStreetMap contributors"),
    ("/html/body/div[1]/div/div/div[2]/ul/li[10]/ul/table/tbody/tr[5]/td[6]/a", "WA"),
    ("/html/body/div[3]/div[4]/div[13]/div/a", "Based on this official offender page"),
    ("/html/body/div[1]/div/div/div[2]/ul/li[6]/ul/table/tbody/tr[5]/td[3]/a", "NM"),
    ("/html/body/div[3]/div[4]/div[29]/div/a[2]", "Based on this official offender page"),
    ("/html/body/div[1]/div/div/div[2]/ul/li[12]/ul/li[4]/ul/table/tbody/tr[2]/td[6]/a", "YT"),
    ("/html/body/div[3]/div[4]/div[5]/div/a[2]", "Based on this official offender page"),
    ("/html/body/div[1]/div/div/div[2]/ul/li[12]/ul/li[4]/ul/table/tbody/tr[1]/td[1]/a", "AB"),
    ("/html/body/div[3]/div[4]/div[4]/div/a[2]", "Based on this official offender page"),
    ("/html/body/div[1]/div/div/div[2]/ul/li[8]/ul/table/tbody/tr[4]/td[5]/a", "NY"),
    ("/html/body/div[3]/div[4]/div[11]/div/a[2]", "Based on this official offender page"),
    ("/html/body/div[1]/div/div/div[2]/ul/li[12]/ul/li[4]/ul/table/tbody/tr[2]/td[5]/a", "SK"),
    ("/html/body/div[3]/div[4]/div[19]/div/a[2]", "Based on this official offender page"),
    ("/html/body/div[1]/div/div/div[2]/ul/li[12]/ul/li[1]/ul/table/tbody/tr[1]/td[7]/a", "CT"),
    ("/html/body/div[3]/div[4]/div[4]/div/a[2]", "Based on this official offender page")
]

# Get the HTML file
html_file = 'downloaded_pages/city-data.html'

# Load the HTML file
with open(html_file, 'r') as f:
    html_content = f.read()

# Create an XML parser
parser = etree.HTMLParser()
tree = etree.fromstring(html_content, parser)

# Extract the text using the XPaths
data = []
for xpath, text in xpaths