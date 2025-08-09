import requests
from bs4 import BeautifulSoup
import re
from dotenv import load_dotenv
import os
load_dotenv

url="https://marco-s.ms.dendai.ac.jp/start/logining"


USER=os.getenv('M_USER')
PASSWORD=os.getenv('PASSWORD')

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