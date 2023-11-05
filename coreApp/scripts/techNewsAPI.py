import requests
import random

url='https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=01a425686ae74b939601e6adf09e9b7b'
response=requests.get(url)

def getTechNews():
  r=random.sample(range(len(response.json()['articles'])),5)
  news_articles=[]
  for i in r:
    news_articles.append({'title':response.json()['articles'][i]['title'],'url':response.json()['articles'][i]['url']})
  
  return news_articles

print(getTechNews())


