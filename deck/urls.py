from django.conf.urls import url
from os import name
from . import views

urlpatterns = [
    url('',views.welcome,name='welcome'),
    url('images/',views.images,name='images'),
    url('search/',views.search_results,name='search_results'),
    url('picha/<int:image_id>/',views.image,name='imageid')
]
