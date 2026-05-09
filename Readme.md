1.  This python code scrapes job data from " <https://realpython.github.io/fake-jobs/>" using requests and beautifulSoup4.

2.  It extracts job details and saves them to 'jobs.csv'.

3.  The code will ask to enter keyword. Input the keyword 'python'.

4.  Output file 'jobs.csv' will be generated in the same folder.

5.  Looping Through Pages : A 'for' loop iterates through page numbers 1 to 5. For each iteration, the URL is updated and 'time.sleep(1)' adds a 1- second delay to respect the server.

6.  Scraping Logic

- HTTP Requests: Uses 'requests.get()' with browser headers to fetch HTML pages and avoid blocking.

- HTML Parsing: 'BeautifulSoup' with parser finds all job cards using 'soup.find_all()' .

- Data Extraction: For each job, extracts Title, Company, Location, Salary, and URL. Handles missing fields with try/except blocks.

- Rate Limiting: 'time.sleep(1)' adds a 1 second delay between page requests to respect the server.

- CSV Export: Built in 'csv.writer' writes data to 'jobs.csv'. writer.writerow() creates the header row first, then writes all job data rows with UTF-8 encoding.

Notes

The script includes error handling for failed requests. All external dependencies are listed in 'requirements.txt'
