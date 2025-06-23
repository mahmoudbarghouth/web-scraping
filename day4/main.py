from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from charset_normalizer.constant import UTF8_MAXIMAL_ALLOCATION

# https://wuzzuf.net/search/jobs/?q=mechanical+engineer&a=navbl"
# https://wuzzuf.net/search/jobs/?a=navbl&q=mechanical%20engineer&start=1
# https://wuzzuf.net/search/jobs/?a=navbl&q=mechanical%20engineer&start=2
# https://wuzzuf.net/search/jobs/?a=navbl&q=mechanical%20engineer&start=10


url="https://wuzzuf.net/search/jobs/?q=mechanical+engineer&a=navbl"
with urlopen(url) as response:
    client=response.read()
    response.close()


soup=bs(client,"html.parser")

container =soup.find_all("div",{"class":"css-1gatmva e1v1l3u10"})
f=open("data.txt","w")
headers="job_title ,company ,company_location ,job_time ,experience_needed \n"
f.write(headers)

for container in container:
    job_title=container.find("a",{"class":"css-o171kl"}).text.strip()

    company=container.find("a",{"class":"css-17s97q8"}).text.strip()

    job_location=container.find("span",{"class":"css-5wys0k"}).text.strip()

    job_time = container.find("span", {"class": "css-1ve4b75 eoyjyou0"}).text.strip()

    ex=container.find_all("div")
    experience=ex[-1].find("span").text.strip()


    f.write(job_title + "," + company + "," + job_location + "," + job_time + "," + experience+ "\n")



for i in range(1,11):
    url=f"https://wuzzuf.net/search/jobs/?a=navbl&q=mechanical%20engineer&start={i}"

    with urlopen(url) as response:
        client = response.read()
        response.close()

    soup = bs(client, "html.parser")

    container = soup.find_all("div", {"class": "css-1gatmva e1v1l3u10"})



    for container in container:
        job_title = container.find("a", {"class": "css-o171kl"}).text.strip()

        company = container.find("a", {"class": "css-17s97q8"}).text.strip()

        job_location = container.find("span", {"class": "css-5wys0k"}).text.strip()

        job_time = container.find("span", {"class": "css-1ve4b75 eoyjyou0"}).text.strip()

        ex = container.find_all("div")
        experience = ex[-1].find("span").text.strip()


        f.write(job_title + "," + company + "," + job_location + "," + job_time + "," + experience + "\n")

f.close()