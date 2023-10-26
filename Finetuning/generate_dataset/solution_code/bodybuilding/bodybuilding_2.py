import csv
from lxml import html

# Define the target HTML file path
html_file_path = "downloaded_pages/bodybuilding.html"

# Define the XPaths of the customer testimonials
testimonials_xpaths = [
    "/html/body/section/main/bb-testimonials-slider/section/bb-testimonials-slide[1]/div/article/p",
    "/html/body/section/main/bb-testimonials-slider/section/bb-testimonials-slide[2]/div/article/p",
    "/html/body/section/main/bb-testimonials-slider/section/bb-testimonials-slide[3]/div/article/p"
]

# Scrape the testimonials from the HTML file using the XPaths
tree = html.parse(html_file_path)
testimonials = [tree.xpath(xpath)[0].text_content() for xpath in testimonials_xpaths]

# Save the scraped data as a CSV file
with open("scraped_data.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Testimonial"])
    writer.writerows([[testimonial] for testimonial in testimonials])