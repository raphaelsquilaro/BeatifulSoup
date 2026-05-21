#Author: Raphael Campos Squilaro
#Project: raspagem de dados

#realizing imports necesseary
from bs4 import BeautifulSoup

#open the index.html
with open ("index.html" , "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

#reading the site
site = BeautifulSoup(conteudo, 'html.parser')

#searching all elements by container card
produtos = site.find_all('div' , class_='card')

#loop for products
for produto in produtos:
    nome = produto.find('div' , class_='nome').text.strip()
    preco = produto.find('div' , class_='preco').text.strip()
    if (nome == "Notebook Gamer"):
        print(f"O nome do produto é: {nome} e seu preço é: {preco}")