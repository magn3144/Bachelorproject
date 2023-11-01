import csv
from bs4 import BeautifulSoup

# Define the HTML elements and their XPaths
elements = [
    {
        "element": "a id=\"archive-link-link\"",
        "xpath": "/html/body/div[1]/div/ul/li[1]/a"
    },
    {
        "element": "a class=\"enabled\" id=\"doodle-newer\"",
        "xpath": "/html/body/div[2]/div/a[2]"
    },
    {
        "element": "h3 This Doodle's Reach",
        "xpath": "/html/body/div[2]/div/ul/li[3]/h3"
    },
    {
        "element": "div class=\"time\"",
        "xpath": "/html/body/div[2]/div/ul/li[1]/div/div"
    },
    {
        "element": "h2 Celebrating Papeda",
        "xpath": "/html/body/div[2]/div/ul/li[1]/div/h2"
    },
    {
        "element": "p So how does one make papeda? After removing the fl",
        "xpath": "/html/body/div[2]/div/ul/li[2]/div/div/p[3]"
    },
    {
        "element": "a id=\"about-link\"",
        "xpath": "/html/body/div[1]/div/ul/li[2]/a"
    },
    {
        "element": "h3 This day in history",
        "xpath": "/html/body/div[2]/div/ul/li[4]/div/h3"
    },
    {
        "element": "h3 More Doodles",
        "xpath": "/html/body/div[2]/div/div[2]/h3"
    }
]

# Define the target page URL, category, local path, and task
target_url = "https://www.google.com"
category = "Educational Websites"
local_path = "downloaded_pages/google.html"
task = "About"

# Open the local HTML file and create a BeautifulSoup object
with open(local_path) as file:
    soup = BeautifulSoup(file, "html.parser")

# Find the element with the target task using its XPath
target_element = soup.find("a", id="about-link")

# Extract the title of the "About" section
about_title = target_element.get_text(strip=True)

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["URL", "Category", "Task", "About Title"])
    writer.writerow([target_url, category, task, about_title])