from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=options)

base_url = "https://kr.indeed.com/jobs"
search_term = "python"

browser.get(f"{base_url}?q={search_term}")
soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul",class_="jobsearch-ResultsList")
#print("job_list? ",job_list)
jobs = job_list.find_all('li', recursive=False)
print(len(jobs))
print("//////")

while (True):
    pass