from celery import shared_task

from django.db import IntegrityError

from newsapi import NewsApiClient
from datetime import datetime

from get_news.models import News

@shared_task
def get_news():
    # peticion unica a la api de noticias 
    newsapi = NewsApiClient(api_key='3fe6ca8bcb77487ebd2beee593559b14')
    top_headlines = newsapi.get_top_headlines(country='us')
    articles = top_headlines['articles']
    
    for art in articles:
        try:
            new = News.objects.create(
                title = art['title'],
                author = art['author'],
                description = art['description'],
                url = art['url'],
                public_date = datetime.strptime(art['publishedAt'], '%Y-%m-%dT%H:%M:%SZ'),
                image = art['urlToImage'],
            )
            new.save()
        except IntegrityError:
                pass