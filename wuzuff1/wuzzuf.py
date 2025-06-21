from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

url="https://wuzzuf.net/search/jobs/?q=production+engineer&a=navbl"
with urlopen(url) as response:
    html=response.read()
    response.close()

soup =bs(html,'html.parser')
containers=soup.find_all("div", {"class":"css-1gatmva e1v1l3u10"})

f=open('production_engineer_jobs_in_wuzuff.csv','w')
headers="job_title,company_name,copany_location,job_type,experience needed\n"
f.write(headers)

for container in containers:
    job_title=container.find("h2", {"class": "css-m604qf"})
    # print(job_title.text)
    company_name=container.find("a", {"class": "css-17s97q8"})
    # print(company_name.text)
    location=container.find("span", {"class": "css-5wys0k"})
    # print(location.text)
    job_time=container.find("span", {"class": "css-1ve4b75 eoyjyou0"})
    # print(job_time.text)
    exp=container.find_all("div")
    # print(len(exp))
    experience=exp[-1].find("span")
    # print(experience.text)
    # print("-----"*10)
    f.write(job_title.text + "," + company_name.text + "," + location.text + "," +job_time.text + "," + experience.text + "\n")
f.close()