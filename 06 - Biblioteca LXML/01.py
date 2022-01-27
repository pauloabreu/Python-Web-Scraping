from lxml import etree

elemento = etree.Element("Teste")
elemento.text = "Este é o texto da tag teste"

print(elemento.tag)


'''
Criando elemento simples
'''