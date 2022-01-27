from lxml import html, etree
import requests

'''
Usando o XPATH
'''

pagina = requests.get(url="https://www.pythonparatodos.com.br/formulario.html", headers={"User-Agent": "Mozilla 5.0"})
tree = html.fromstring(pagina.text)
table = tree.xpath('/html/body/form/table')

for x in table:
    print(etree.tostring(x, pretty_print=True).decode("utf-8"))