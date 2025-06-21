from urllib.request import urlopen
from bs4 import BeautifulSoup as bs



url="https://wuzzuf.net/search/jobs/?q=programing&a=navbl"
with urlopen(url) as response:
    html=response.read()
    response.close()
soup=bs(html,'html.parser')
containers=soup.find_all('div',{"class":"css-1gatmva e1v1l3u10"})
f=open("jobs_for_programing_in_wuzuff.csv","w")
headers="job_title,company_name,location,job_time,experience\n"
f.write(headers)
# print(len(containers))
for container in containers:
    job_title=container.find('h2',{"class":"css-m604qf"}).text
    # print(job_title)
    company_name=container.find("a",{"class":"css-17s97q8"}).text
    # print(company_name)
    location=container.find("span",{"class":"css-5wys0k"}).text
    # print(location)
    jobetime=container.find("a",{"class":"css-n2jc4m"} ).text
    # print(jobetime)
    exp=container.find_all("div")
    # print(exp[-1])
    exper = exp[-1].find("span")
    if exper:
        experience=exper.text
        # print(experience)
    f.write(job_title + "," + company_name + "," + location + "," + jobetime + "," + experience +'\n' )
f.close()

