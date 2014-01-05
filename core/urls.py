from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'), # Home view for a logged in user
    url(r'^faq/$', views.faq_view, name='faq'), # Home view for a logged in user
    url(r'^collections/$', views.collections_view, name='collections_view'), # show all collections
    #url(r'^(?P<username>\w+)/', views.user_view, name='user_view'),
    #url(r'^(?P<username>\w+)/edit/', views.user_edit, name='user_edit'),
    #url(r'^(?P<username>\w+)/(?P<collectionname>\w+)/', views.collection_view, name='collection_view'),
    #url(r'^(?P<username>\w+)/(?P<collectionname>\w+)/edit/', views.collection_edit, name='collection_edit'),
    #url(r'^(?P<username>\w+)/(?P<collectionname>\w+)/(?P<bookmark_id>\d+)/', views.bookmark_view, name='bookmark_view'),
    #url(r'^(?P<username>\w+)/(?P<collectionname>\w+)/(?P<bookmark_id>\d+)/edit/', views.bookmark_edit, name='bookmark_edit'),

    # /username/tags/
    # /username/tags/edit/
    # /login
    # /signup
)
