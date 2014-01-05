from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import Count

from core.models import UserProfile, Collection, Bookmark, Tag

"""
url(r'^$', views.index, name='index'),
url(r'^collections/$', views.collections_view, name='collections_view'), # show all collections
url(r'^(?P<username>\w+)/', views.user_view, name='user_view'),
url(r'^(?P<username>\w+)/edit/', views.user_edit, name='user_edit'),
url(r'^(?P<username>\w+)/(?P<collectionname>\w+)/', views.collection_view, name='collection_view'),
url(r'^(?P<username>\w+)/(?P<collectionname>\w+)/edit/', views.collection_edit, name='collection_edit'),
url(r'^(?P<username>\w+)/(?P<collectionname>\w+)/(?P<bookmark_id>\d+)/', views.bookmark_view, name='bookmark_view'),
url(r'^(?P<username>\w+)/(?P<collectionname>\w+)/(?P<bookmark_id>\d+)/edit/', views.bookmark_edit, name='bookmark_edit'),
"""

def index(request):
    #collections_with_counts = Collection.objects.annotate(Count('bookmark'))
    #context = {'collections_with_counts': collections_with_counts}
    return render(request, 'core/index.html')

def home(request):
    """ The home view for a logged in user. """
    return render(request, 'core/home.html')

def faq_view(request):
    """ The FAQ view. """
    return render(request, 'core/faq.html')

def collections_view(request):
    collections_w_bmark_counts = []
    collections = Collection.objects.all()
    for collection in collections:
        dict = {}
        dict['name'] = collection.name
        dict['count'] = collection.bookmark_set.count()
        collections_w_bmark_counts.append(dict)
    return render(request, 'core/collections_view.html', {'collections_w_bmark_counts': collections_w_bmark_counts})

"""
def body_edit(request, body_id):
    if request.method == 'GET':
        body = get_object_or_404(KnowledgeBody, pk=body_id)
        return render(request, 'km/body_edit.html', {'body': body})
    else:
        b = get_object_or_404(KnowledgeBody, pk=body_id)
        try:
            delete_selected = b.knowledgebranch_set.get(pk=request.POST['branch'])
        except (KeyError, KnowledgeBranch.DoesNotExist):
            # Redisplay the poll voting form.
            return render(request, 'km/body_edit.html', {
                'body': b,
                'error_message': "You didn't check any boxes.",
            })
        else:
            delete_selected.delete()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('km:body_detail', args=(b.id,)))
"""
