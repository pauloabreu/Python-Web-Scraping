from inspect import Attribute
from pydoc import html
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.udemy.com")
print(f"Html: {html}")

try:     
    html = urlopen("http://www.udemy.com/erro")
    print(f"Htm2: {html}")
except HTTPError as error:
    print(error)

try:
    html = urlopen("http://www.sdadsasd.com")
    print(f"Htm3: {html}")
except URLError as error:
    print(error)

try:
    html = urlopen("http://www.udemy.com")
    bsObj = BeautifulSoup(html.read(), "html.parser")
    resultado  = bsObj.tag_nao_existe.tag_vai_dar_erro
    print(resultado)
except AttributeError as error:
    print(error)