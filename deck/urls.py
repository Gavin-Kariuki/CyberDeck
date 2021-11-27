from django.conf.urls import url
from os import name
from . import views
from django.conf import settings


urlpatterns = [
    url('',views.welcome,name='welcome'),
    url('images/',views.mapicha,name='images'),
    url('search/',views.search_results,name='search_results'),
    url('picha/<int:image_id>/',views.picha,name='imageid')
]
