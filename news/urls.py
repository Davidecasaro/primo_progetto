from django.urls import path
from .views import *

app_name='news'

urlpatterns=[
    path('',index,name="indexNews"),
    path('homepageNews',home,name="homepageNews"),
    path("articoli",articoloDetailView,name="articoli_detail"),
    path("articoli/<int:pk>",articoloDetailView,name="articoli_detail"),  
    path("lista_articoli/",listaArticoli,name="lista_articoli"), path("lista_articoli/<int:pk>",listaArticoli,name="lista_articoli_giornalista"),
    
]