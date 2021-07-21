import requests as r 
from bs4 import BeautifulSoup

uri = "https://www.tesla.com/en_SG/findus/list/superchargers/Singapore"


def fetch():
    scList = []
    res = r.get(uri)
    # print(res)
    res = res.text
    # print(res)
    soup = BeautifulSoup(res, features='lxml')
    # print(soup)
    tags = soup.find_all("address")
    for tag in tags:
        scList.append({
            "name" : tag.a.text,
            "url" : tag.a['href']
        })
    return scList
# fetch()