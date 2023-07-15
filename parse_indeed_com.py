"""
https://www.reddit.com/r/learnpython/comments/udlgfz/please_help_fix_web_scraping_code_bs4_python/
"""

import requests
from bs4 import BeautifulSoup


url = "https://au.indeed.com/jobs?q=Software%20Engineer&l=Adelaide%20Region%20SA&radius=100&vjk=ca36e39d39db9210"
r = requests.get(url)

webpage = r.content
soup = BeautifulSoup(webpage, "html.parser")

lst_jobs = []
job_card = soup.find_all("div", class_="job_seen_beacon")
for item in job_card:
    job = {"salary": "N/A"}
    elem_title = item.find("span", title=True)
    if elem_title:
        job["title"] = elem_title.text.strip()
    elem_company = item.find("span", class_="companyName")
    if elem_company:
        job["company"] = elem_company.text.strip()
    elem_salary = item.find("div", class_="salary-snippet", recursive=True)
    if elem_salary:
        job["salary"] = elem_salary.text.strip()
    lst_jobs.append(job)

for each in lst_jobs:
    print(each)
