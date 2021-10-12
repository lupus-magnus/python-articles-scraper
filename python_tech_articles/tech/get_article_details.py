import json
import requests
from bs4 import BeautifulSoup

endpoint = 'https://www.tecmundo.com.br/mercado/226715-vagas-emprego-auxilio-psicologico-crescem-1-215-2021.htm'


source = requests.get(endpoint).content

soup = BeautifulSoup(source, 'lxml')

author_name = soup.find('a', class_='tec--author__info__link').text
author_url =  soup.find('a', class_='tec--author__info__link')['href']

article_title = soup.find('h1', id="js-article-title").text
article_body = soup.find('div', class_="tec--article__body").text
article_hero = soup.find('img', class_="tec--article__image")['data-src']

article_obj = {
    "article": {
        "title": article_title,
        "body": article_body,
        "image": article_hero
    },
    "author": {
        "name": author_name,
        "url": author_url
    }
}

json_results = json.dumps(article_obj,  ensure_ascii=False).encode('utf-8')
json_file = open('article.json', 'w')
json_file.write(json_results.decode())
json_file.close()