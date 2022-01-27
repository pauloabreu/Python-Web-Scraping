from pprint import pprint
from lxml import etree

'''
Criando Sub Elementos
'''

clientes = etree.Element("clientes")
cliente1 = etree.SubElement(clientes, "cliente")

nome1 = etree.SubElement(cliente1, "nome")
nome1.text = "Nome do cliente"

idade1 = etree.SubElement(cliente1, "idade")
idade1.text = "32"

sexo1 = etree.SubElement(cliente1, "sexo")
sexo1.text = "Masculino"

cpf1 = etree.SubElement(cliente1, "cpf")
cpf1.text = "012.345.678-90"

pprint(etree.tostring(clientes))