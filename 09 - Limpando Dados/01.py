from cgitb import text
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string

def limpar_texto(texto):
    texto = texto.strip()
    texto_limpo = []
    texto = re.sub("\n+", " ", texto)
    texto = re.sub(" +", " ", texto)
    texto = texto.replace(u"\xa0", u"")
    texto = re.sub("\[[0-9]*\]", "", texto)
    texto = texto.split(" ")

    for item in texto:
        item = item.strip()
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'e' or item.lower() == 'o'):
            texto_limpo.append(item)

    return texto_limpo

html = urlopen("https://pt.wikipedia.org/wiki/Python")
bsObj = BeautifulSoup(html)
conteudo = bsObj.find("div", {"id":"mw-content-text"}).get_text()
#conteudo = conteudo.split(" ")
conteudo = limpar_texto(conteudo)
print(conteudo)