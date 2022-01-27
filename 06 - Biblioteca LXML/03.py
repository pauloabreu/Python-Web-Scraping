from lxml import etree

'''
Trabalhando com elementos/listas
'''

clientes = etree.Element("clientes")

cliente1 = etree.SubElement(clientes, "cliente")
nome1 = etree.SubElement(cliente1, "nome")
nome1.text = "Nome do cliente"

cliente2 = etree.SubElement(clientes, "cliente2")
nome2 = etree.SubElement(cliente2, "nome")
nome2.text = "Nome do cliente 2"

cliente3 = etree.SubElement(clientes, "cliente3")
nome3 = etree.SubElement(cliente3, "nome")
nome3.text = "Nome do cliente 3"

print("Total de clientes: ", len(clientes))

cliente_dois = clientes[1]

print("Tag clientes[1]", cliente_dois.tag)

for x in clientes:
    print(x.tag)