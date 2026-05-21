#Author: Raphael Campos Squilaro
#Project: raspagem de dados

#realizing imports necesseary
from bs4 import BeautifulSoup

#open the index.html
with open ("index.html" , "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

#reading the site
site = BeautifulSoup(conteudo, 'html.parser')

# Mudança aqui: find busca apenas o primeiro card encontrado
produto = site.find('div' , class_='card')

# Se o produto existir, extrai e printa as informações
if produto:
    nome = produto.find('div' , class_='nome').text.strip()
    preco = produto.find('div' , class_='preco').text.strip()
    print("----------------------------")
    print(f"O nome do produto é: {nome} e seu preço é: {preco}")
