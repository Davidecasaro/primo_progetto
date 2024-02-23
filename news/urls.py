from django.urls import path
from .views import *

app_name='news'

urlpatterns=[
    path('',index,name="indexNews"),
    path('homepageNews',home,name="homepageNews"),
    path("articoli",articoloDetailView,name="articoli_detail"),
    path("articoli/<int:pk>",articoloDetailView,name="articoli_detail"),  
    path("giornalisti",giornalistaDetailView,name="giornalisti_detail"),
    path("giornalisti/<int:pk>",giornalistaDetailView,name="giornalisti_detail"),
    path("lista_articoli/",listaArticoli,name="lista_articoli"), 
    path("lista_articoli/<int:pk>",listaArticoli,name="lista_articoli_giornalista"),
    path("lista_giornalisti/",listaGiornalisti,name="lista_giornalisti"),
    path("lista_giornalisti/<int:pk>",listaGiornalisti,name="lista_giornalisti"),
    path("query/",queryBase,name="query"),
    
    path('lista_giornalisti_api/',giornalisti_list_api, name="giornalisti_list_api"),
    path('giornalista_api/<int:pk>',giornalista_api, name="giornalista_api"),
    path('lista_articoli_api/',articoli_list_api, name="articoli_list_api"),
    path('articolo_api/<int:pk>',articolo_api, name="articolo_api"),

]