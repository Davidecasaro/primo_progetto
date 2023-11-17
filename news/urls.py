from django.urls import path
from .views import home, articoloDetailView

app_name='news'

urlpatterns=[
    path('',home,name="indexNews"),
    path('homepageNews',home,name="homepageNews"),
    path("articoli/<int:pk>",articoloDetailView,name="articolo_detail"),
]