from requests import get
from bs4 import BeautifulSoup

main_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"
response = get(f"{main_url}{search_term}")
if not response.status_code == 200:
    print("Can't request the website!")
else:
    soup = BeautifulSoup(response.text ,"html.parser")
    jobs = soup.find_all('section', class_="jobs")
    for job in jobs:
        job_post = job.find_all("li")
        job_post.pop(-1)
        for post in job_post:
            anchors = post.find_all('a')
            anchor = anchors[1]
            link = anchor['href']
            company, kind, region = anchor.find_all('span', class_="company")
            title = anchor.find('span', class_='title')
            print(company, kind, region, title)
            print("/////////////////////")
            print("/////////////////////")