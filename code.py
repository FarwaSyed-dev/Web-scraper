import requests
from bs4 import BeautifulSoup
import csv
import time

url = "https://realpython.github.io/fake-jobs/"
# website link 
keyword = input("Enter keyword: ")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
# create csv file
file = open("jobs.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(file)
writer.writerow(["Title", "Company", "Location", "Salary", "URL"])

# Loop through first 5 pages
for page in range(1, 6):
    if page == 1:
        current_url = url
    else:
        current_url = f"{url}?page={page}"
    
    print(f"Scraping page {page}...")
     # Get webpage
    response = requests.get(current_url, headers=headers, timeout=10)
    
    if response.status_code != 200:
        print(f"Page {page} blocked. Stopping.")
        break
    
      # read html of page
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("div", class_="card-content")
    
    if not jobs:
        print(f"No jobs on page {page}. Stopping.")
        break
  # find all jobs
    for job in jobs:
        title = job.find("h2", class_="title").text.strip()

        if keyword.lower() not in title.lower():
            continue

        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        link = job.find("a")["href"]
        writer.writerow([title, company, location, "Not Mentioned", link])
    
    time.sleep(1)

file.close()
print("All Jobs saved in jobs.csv")