import requests
from bs4 import BeautifulSoup
import re

url="https://marco-s.ms.dendai.ac.jp/start/logining"


USER="24AJ116"
PASSWORD="h1720050509r1k1R!K!"

session=requests.session()

login_info={
    "login":USER,
    "password":PASSWORD
}

res=session.post(url,data=login_info)
res.raise_for_status()

print(res.text)

print("-----------------------------------------")
url="https://marco-s.ms.dendai.ac.jp/start/student/search/searchTimestamp"


headers = {
    "Referer": "https://marco-s.ms.dendai.ac.jp/start/common/user/userStartPage", 
    "User-Agent": "Mozilla/5.0" 
}       


res=session.get(url,headers=headers)
res.raise_for_status()

print(res.text) 

url="https://marco-s.ms.dendai.ac.jp/start/student/search/searchDetail/dakokuInfo"

headers={
    re
}
res=session.get(url,)