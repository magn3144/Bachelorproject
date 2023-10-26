import csv
from bs4 import BeautifulSoup

# Open the HTML file
with open("downloaded_pages/ziprecruiter.html", "r") as file:
    html_content = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, "html.parser")

# Find all job listings
job_listings = soup.find_all("div", class_="jobList-description")

# Extract the salary timeframes from each job listing
salary_timeframes = []
for job in job_listings:
    timeframe = job.find("span", class_="jobList-timeframe")
    if timeframe:
        salary_timeframes.append(timeframe.text.strip())

# Save the data in a CSV file
with open("scraped_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Salary Timeframe"])
    writer.writerows(zip(salary_timeframes))