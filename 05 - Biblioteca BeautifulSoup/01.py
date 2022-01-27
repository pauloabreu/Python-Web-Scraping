from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://localhost/meusite/")
bsObj = BeautifulSoup(html.read(), "html.parser")

print(bsObj.h1)
print(bsObj.title)
print(bsObj.find_all("h1"))