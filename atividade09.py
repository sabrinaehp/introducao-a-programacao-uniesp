import requests
import csv
from bs4 import BeautifulSoup


f = csv.writer(open('nomes_artistas.csv', 'w'))
f.writerow(['Name', 'Link'])

paginas = []
paginas2 = []
for i in range(1, 42):
    url = f'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anC{str(i)}.htm'
    paginas.append(url)

for item in paginas:
    pagina = requests.get(item)
    soup = BeautifulSoup(pagina.text, 'html.parser')

    ultimos_links = soup.find(class_='AlphaNav')
    ultimos_links.decompose()

    lista_nome_artistas = soup.find(class_='BodyText')
    itens_artista_nome = lista_nome_artistas.find_all('a')

    for nome_artista in itens_artista_nome:
        names = nome_artista.contents[0]
        links = 'https://web.archive.org' + nome_artista.get('href')

        f.writerow([names, links])