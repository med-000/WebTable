import requests
from bs4 import BeautifulSoup
import re

url="https://els.sa.dendai.ac.jp/webclass/login.php"

response=requests.get(url)

USER="24aj116"
PASSWORD="h1720050509r1k1R!K!"

session=requests.session()

login_info={
    "username":USER,
    "val":PASSWORD
}

res=session.post(url,data=login_info)
res.raise_for_status()


print(res.text)
res_txt=res.text

soup=BeautifulSoup(res_txt,"html.parser")
print(soup)

elems=soup.find("script")
print(elems)
elems_text=elems.text
print(re.search(r'window\.location\.href="([^"]+)"', elems_text))
match=re.search(r'window\.location\.href="([^"]+)"', elems_text)
print(match.group(1))
url_res="https://els.sa.dendai.ac.jp"+str(match.group(1))
print(url_res)
response=session.get(url_res)
print(response.text)
#str_elems=str(re.findall('".*"',elems.text))
#print("www"+str_elems)
