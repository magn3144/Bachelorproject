import csv
from lxml import etree

# Define the target HTML file path
html_file_path = "downloaded_pages/4chan.html"

# Define the category
category = "Social Media"

# Define the task
task = "Extract all file labels and their XPaths"

# Define the list of HTML elements with their corresponding XPaths
elements_with_xpaths = [
    ("<a>/bant/ - International/Random</a>", "/html/body/form/table[2]/tbody/tr[2]/td[2]/a"),
    ("<a>jp</a>", "/html/body/div[1]/div[1]/span[1]/a[33]"),
    ("<div class=\"boardTitle\">/o/ - Auto</div>", "/html/body/div[2]/div[2]"),
    ("<span>Your web browser must have JavaScript enabled in o</span>", "/html/body/noscript/div/span"),
    ("<span class=\"button\">Top</span>", "/html/body/div[8]/span[1]/span[3]/span"),
    ("<td class=\"blotter-date\">10/04/16</td>", "/html/body/form/table[2]/tbody/tr[3]/td[1]"),
    ("<h4>Janitor acceptance emails will be sent out over th</h4>", "/html/body/div[5]/h4"),
    ("<a>/vip/ - Very Important Posts</a>", "/html/body/form/table[2]/tbody/tr[3]/td[2]/a"),
    ("<a>po</a>", "/html/body/div[1]/div[1]/span[1]/a[40]"),
    ("<span class=\"absBotDisclaimer\">All trademarks and copyrights on this page are own</span>", "/html/body/div[9]/span"),
    ("<span class=\"button\">Bottom</span>", "/html/body/div[8]/div[1]/div[1]/span[1]/span[3]/span"),
    ("<td>Options</td>", "/html/body/form/table[1]/tbody/tr[2]/td[1]"),
    ("<a>Disable Mobile View / Use Desktop Site</a>", "/html/body/div[9]/div[1]/span[1]/a"),
    ("<a id=\"filters-clear-hidden-bottom\">Show</a>", "/html/body/div[8]/span[3]/span[2]/a"),
    ("<span class=\"button\" id=\"togglePostFormLinkMobile\">Start a New Thread</span>", "/html/body/div[3]/span/span"),
    ("<td>Subject</td>", "/html/body/form/table[1]/tbody/tr[3]/td[1]"),
    ("<a>Enable Mobile View / Use Mobile Site</a>", "/html/body/div[9]/div[1]/span[2]/a"),
    ("<a>fa</a>", "/html/body/div[1]/div[1]/span[1]/a[28]"),
    ("<span id=\"jscnf2\">🎉</span>", "/html/body/div[5]/h2/span[2]"),
    ("<td class=\"blotter-date\">05/04/17</td>", "/html/body/form/table[2]/tbody/tr[2]/td[1]"),
    ("<a>Feedback</a> •", "/html/body/div[9]/div[2]/a[2]"),
    ("<span class=\"button\" id=\"qf-clear\">✖</span>", "/html/body/div[8]/div[1]/div[2]/span[6]/span"),
    ("<td>File</td>", "/html/body/form/table[1]/tbody/tr[6]/td[1]"),
    ("<a>v</a>", "/html/body/div[1]/div[1]/span[1]/a[8]"),
]

# Create a list to store the extracted data
scraped_data = []

# Parse the HTML file
root = etree.parse(html_file_path, etree.HTMLParser())

# Extract file labels and their XPaths from the target page
for element, xpath in elements_with_xpaths:
    try:
        file_label = root.xpath(xpath)[0].text.strip()
        scraped_data.append((file_label, xpath))
    except IndexError:
        pass

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["File Label", "XPath"])
    writer.writerows(scraped_data)