import requests
from bs4 import BeautifulSoup

r = requests.get("https://www26.atwiki.jp/gcmatome/pages/24.html")

soup = BeautifulSoup(r.content, "html.parser")
l=soup.select('td a')

with open("ps3.txt",mode="w",encoding="utf-8") as f:
    for b in l:
        f.write("{}\n".format(b.getText()))
