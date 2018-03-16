""" Defines URL patterns for porfolio """

from django.conf.urls import url

from . import views

urlpatterns = [
    #Home page
    url(r'^$', views.index, name='index'),
]