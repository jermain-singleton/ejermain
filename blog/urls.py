""" Defines URL patterns for porfolio """

from django.conf.urls import url

from . import views


urlpatterns = [
    #Show the post
    url(r'^posts/$', views.posts, name='posts'),
    #Page for a single post
    url(r'^posts/(?P<post_id>\d+)/$', views.post, name='post'),
    #Page for adding a new post
    url(r'^new_post/$', views.new_post, name='new_post'),
    #Page for adding a new entry
    url(r'^new_entry/(?P<post_id>\d+)/$', views.new_entry, name='new_entry'),
    #Page for editing entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]