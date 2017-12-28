from django.conf.urls import url
from . import views

app_name = 'tixy'

urlpatterns = [
    # /tixy/
    url(r'^$', views.index, name='index'),

    # /tixy/<movie_id>/
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^book/(?P<slot_id>[0-9]+)/$', views.book, name='book'),
]
