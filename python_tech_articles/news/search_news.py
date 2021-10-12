import json
import requests
from bs4 import BeautifulSoup

endpoint = "https://search.folha.uol.com.br/?q=arte&site=todos"

source = requests.get(endpoint).content

soup = BeautifulSoup(source, 'lxml')

fetched_news = soup.find_all('li', class_="c-headline--newslist")

results = []

for news_obj in fetched_news:
    title = ' '.join(news_obj.find('h2', class_="c-headline__title").text.split())
    url = news_obj.a['href']
    image = news_obj.find('img',class_="c-headline__image")
    if(image):
        results.append({
            "title": title,
            "url": url,
            "image": image['src'] if image['src'] else "N/A"
        })

#Salvando num arquivo json
json_results = json.dumps(results,  ensure_ascii=False).encode('utf-8')
json_file = open('scraped_news.json', 'w')
json_file.write(json_results.decode())
json_file.close()

print(results)