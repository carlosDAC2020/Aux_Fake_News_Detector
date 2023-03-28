from django.shortcuts import render, HttpResponse
from django.db import IntegrityError

#from newsapi import NewsApiClient
import feedparser
from datetime import datetime

from .models import News

def index(request):
    
    return render(request, 'index.html', {
        "articles": News.objects.all()
    })
    

def news(request):
    # URLs de los feeds RSS
    rss_urls = [
        
        # feeds nacionales 
        # el tiempo 
            # opinion
        'https://www.eltiempo.com/rss/opinion.xml',
        'https://www.eltiempo.com/rss/opinion_editorial.xml',
        'https://www.eltiempo.com/rss/opinion_mas-opinion.xml',
        'https://www.eltiempo.com/contenido/feed',

            # regiones
        'https://www.eltiempo.com/rss/colombia.xml',
        'https://www.eltiempo.com/rss/colombia_barranquilla.xml',
        'https://www.eltiempo.com/rss/colombia_medellin.xml',
        'https://www.eltiempo.com/rss/colombia_cali.xml',
        'https://www.eltiempo.com/rss/colombia_otras-ciudades.xml',

            # mundo
        'https://www.eltiempo.com/rss/mundo.xml',
        'https://www.eltiempo.com/rss/mundo_latinoamerica.xml',
        'https://www.eltiempo.com/rss/mundo_eeuu-y-canada.xml',
        'https://www.eltiempo.com/rss/mundo_europa.xml',
        'https://www.eltiempo.com/rss/mundo_medio-oriente.xml',
        'https://www.eltiempo.com/rss/mundo_asia.xml',
        'https://www.eltiempo.com/rss/mundo_africa.xml',
        'https://www.eltiempo.com/rss/mundo_mas-regiones.xml',
          
            # economia 
        'https://www.eltiempo.com/rss/economia.xml',
        'https://www.eltiempo.com/rss/economia_finanzas-personales.xml ',
        'https://www.eltiempo.com/rss/economia_empresas.xml ',
        'https://www.eltiempo.com/rss/economia_sectores.xml',
        'https://www.eltiempo.com/rss/economia_sector-financiero.xml',

            # deportes 
        'https://www.eltiempo.com/rss/deportes.xml ',
        'https://www.eltiempo.com/rss/deportes_futbol-internacional.xml ',
        'https://www.eltiempo.com/rss/deportes_futbol-colombiano.xml ',
        'https://www.eltiempo.com/rss/deportes_tenis.xml',
        'https://www.eltiempo.com/rss/deportes_ciclismo.xml',
        'https://www.eltiempo.com/rss/deportes_automovilismo.xml',
        'https://www.eltiempo.com/rss/deportes_otros-deportes.xml'
    ]

    i=1
    for url in rss_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            try:
                new = News.objects.create(
                    title = entry.title,
                    description = entry.summary,
                    url =entry.links[0].href,
                    public_date = datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %z'),
                    image = entry.links[1].href if len(entry.links)>1 else ""
                )
                new.save()
            except IntegrityError:
                    pass
           
            i+=1
        
    
    return HttpResponse(f"recibidos {i} articulos ")

    

    

