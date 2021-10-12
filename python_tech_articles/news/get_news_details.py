import json
import requests
from bs4 import BeautifulSoup

endpoint = "https://www1.folha.uol.com.br/poder/2021/10/lewandowski-rejeita-pedido-para-obrigar-alcolumbre-a-marcar-sabatina-de-mendonca-ao-stf.shtml"


source = requests.get(endpoint).content

soup = BeautifulSoup(source, 'lxml')

author = soup.find('strong', class_='c-signature__author')
author_name = ' '.join(author.text.split())
author_url =  author.a['href']

article_title = ' '.join(soup.find('h1', class_="c-content-head__title").text.split())
article_subtitle = ' '.join(soup.find('h2',class_="c-content-head__subtitle").text.split())
article_body = ' '.join(soup.find('div', class_="c-news__body").text.split())

article_obj = {
    "article": {
        "title": article_title,
        "subtitle": article_subtitle,
        "body": article_body,
    },
    "author": {
        "name": author_name,
        "url": author_url
    }
}


json_results = json.dumps(article_obj,  ensure_ascii=False).encode('utf-8')
json_file = open('news_article.json', 'w')
json_file.write(json_results.decode())
json_file.close()