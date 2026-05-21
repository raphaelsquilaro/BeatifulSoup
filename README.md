# 📌 Projeto de Raspagem de Dados com BeautifulSoup

## 👨‍💻 Autor
**Raphael Campos Squilaro**

---

# 📖 Sobre o Projeto

Este projeto demonstra uma raspagem de dados simples utilizando a biblioteca **BeautifulSoup** em Python.

O objetivo é ler um arquivo HTML local (`index.html`), localizar elementos específicos da página e extrair informações de produtos, como nome e preço.

---

# 🛠 Tecnologias Utilizadas

- Python 3
- BeautifulSoup4

---

# 📦 Instalação

Antes de executar o projeto, instale a biblioteca necessária:

```bash
pip install beautifulsoup4
```

---

# 📁 Estrutura do Projeto

```bash
projeto/
│
├── index.html
├── scraping.py
└── README.md
```

---

# 📄 Código do Projeto

```python
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
```

---

# 🚀 Passo a Passo do Funcionamento

## 1️⃣ Importação da Biblioteca

```python
from bs4 import BeautifulSoup
```

Aqui estamos importando o **BeautifulSoup**, responsável por interpretar o HTML e permitir a navegação pelos elementos da página.

---

## 2️⃣ Abertura do Arquivo HTML

```python
with open ("index.html" , "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
```

Nesta etapa:

- O arquivo `index.html` é aberto em modo leitura (`r`);
- O conteúdo HTML é armazenado na variável `conteudo`;
- O `encoding="utf-8"` garante suporte a caracteres especiais.

---

## 3️⃣ Leitura do HTML com BeautifulSoup

```python
site = BeautifulSoup(conteudo, 'html.parser')
```

O BeautifulSoup interpreta o conteúdo HTML usando o parser padrão do Python (`html.parser`).

Isso transforma o HTML em uma estrutura navegável.

---

## 4️⃣ Busca dos Produtos

```python
produtos = site.find_all('div' , class_='card')
```

Aqui o programa procura todas as `<div>` que possuem a classe `card`.

Cada `card` representa um produto da página.

### Exemplo de HTML esperado

```html
<div class="card">
    <div class="nome">Notebook Gamer</div>
    <div class="preco">R$ 5.000</div>
</div>
```

---

## 5️⃣ Loop de Extração dos Dados

```python
for produto in produtos:
```

O programa percorre todos os produtos encontrados.

---

## 6️⃣ Extração do Nome e Preço

```python
nome = produto.find('div' , class_='nome').text.strip()
preco = produto.find('div' , class_='preco').text.strip()
```

### O que acontece aqui:

- `find()` procura o elemento desejado;
- `.text` captura apenas o texto;
- `.strip()` remove espaços extras.

---

## 7️⃣ Filtro do Produto

```python
if (nome == "Notebook Gamer"):
```

O código verifica se o nome do produto é **Notebook Gamer**.

---

## 8️⃣ Exibição do Resultado

```python
print(f"O nome do produto é: {nome} e seu preço é: {preco}")
```

### Saída esperada:

```bash
O nome do produto é: Notebook Gamer e seu preço é: R$ 5.000
```

---

# ✅ Objetivo do Projeto

Este projeto tem como finalidade:

- Aprender conceitos básicos de Web Scraping;
- Trabalhar com HTML usando Python;
- Entender navegação e busca de elementos;
- Extrair dados de páginas HTML.

---

# 📚 Conceitos Aprendidos

- Leitura de arquivos HTML;
- Parsing de HTML;
- Busca de elementos por classe;
- Loops em Python;
- Manipulação de texto;
- Extração de dados estruturados.

---

# 🔥 Melhorias Futuras

Possíveis evoluções do projeto:

- Ler páginas reais da internet usando `requests`;
- Exportar dados para CSV;
- Criar filtros avançados;
- Buscar múltiplos produtos;
- Armazenar informações em banco de dados.

---

# ▶️ Como Executar

Execute o arquivo Python:

```bash
python scraping.py
```

---

# 📄 Licença

Projeto desenvolvido para fins educacionais.
