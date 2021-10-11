import json
import requests
from bs4 import BeautifulSoup

endpoint = "https://www.tecmundo.com.br/busca?q=python"

source = requests.get(endpoint).content

soup = BeautifulSoup(source, 'lxml')

articles = soup.find_all('article', class_='tec--card--medium')

results = []

for article in articles:
    image = article.find('img')['data-src']
    title = str(article.find('a', class_="tec--card__title__link").text)
    url = article.find('a',class_="tec--card__title__link")['href']
    article_obj = {
        'image': image,
        'title': title,
        'url': url
    }
    results.append(article_obj)

for article_obj in results:
    print(article_obj)

# Salvando num arquivo json
json_results = json.dumps(results,  ensure_ascii=False).encode('utf-8')
json_file = open('scraped_articles.json', 'w')
json_file.write(json_results.decode())
json_file.close()

