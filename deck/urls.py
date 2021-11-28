from django.urls import path
from os import name
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.karibu,name='karibu'),
    path('mapicha/',views.mapicha,name='mapicha'),
    path('search/',views.search_results,name='search_results'),
    path('picha/<int:image_id>/',views.picha,name='imageid')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
