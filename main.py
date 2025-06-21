import csv
from re import findall

import requests
from bs4 import BeautifulSoup as bs
from  urllib.request import urlopen
url="https://wuzzuf.net/search/jobs/?a=navbl&q=illustrator&start=0"
client=urlopen(url)
html=client.read()
client.close()
soup=bs(html,'html.parser')
containers=soup.find_all("div",{"class":"css-1gatmva e1v1l3u10"})

f=open("data_wazuff.csv","w")
header="job_title,company_name,jobe_type\n"
f.write(header)

for container in containers:
    jtitle=container.find_all('h2',{"class":"css-m604qf"})
    title=jtitle[0].text
    jcompany=container.find_all("a",{"class":"css-17s97q8"})
    copany_name=jcompany[0].text.strip()
    jtime=container.find_all("a",{"class":"css-n2jc4m"})
    jobe_type=jtime[0].text.strip()
    f.write(title +","+ copany_name +","+ jobe_type + "\n")



