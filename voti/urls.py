from django.urls import path
from voti.views import *

app_name="voti"
urlpatterns=[
    path("wiew_a",wiew_a,name="wiew_a"),
    path("wiew_b",wiew_b,name="wiew_b"),
    path("wiew_c",wiew_c,name="wiew_c"),
    path("wiew_d",wiew_d,name="wiew_d"),
    path('',indexVoti,name='indexVoti'),
    ]