from selenium import webdriver
from bs4 import BeautifulSoup

def get_page_count(keyword):
    driver = webdriver.Chrome()
    driver.get(f'https://kr.indeed.com/jobs?q={keyword}')
    soup=BeautifulSoup(driver.page_source, 'html.parser')
    pagination = soup.find('nav', class_='css-jbuxu0')
    if pagination == None:
        return 1
    pages = pagination.find_all('div', recursive=False)
    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count


def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("Found", pages, "pages")
    for page in range(pages):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome("./chromedriver.exe", options=options)
        driver.get(f'https://kr.indeed.com/jobs?q={keyword}&start={page*10}')
        finalurl = (f'https://kr.indeed.com/jobs?q={keyword}&start={page*10}')

    print('requesting', finalurl)
    if finalurl == None:
        print('Cant request page')
    else:
        results = []
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        job_list = soup.find('ul', class_='jobsearch-ResultsList')
        jobs = job_list.find_all('li', recursive=False)
        for job in jobs:
            zone = job.find('div', class_='mosaic-zone')
            if zone == None:
                anchor = job.select_one('h2 a')
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find('span', class_='companyName')
                location = job.find('div', class_='companyLocation')
                job_data = {
                    'link': f'https://kr.indeed.com{link}',
                    'company': company.string,
                    'position': title,
                    'location': location.string
                }
    results.append(job_data)

jobs = extract_indeed_jobs('python')
print(jobs)