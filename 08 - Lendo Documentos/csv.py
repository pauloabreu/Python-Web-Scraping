from urllib.request import urlopen
from io import StringIO
import csv

url = input("Informe o caminho do arquivo CSV: ")
dados = urlopen(url).read().decode(encoding='utf-8', errors='ignore')
arqDados = StringIO(dados)
#csvReader = csv.reader(arqDados)
csvReader = csv.DictReader(arqDados)

for linha in csvReader:
    print(linha)