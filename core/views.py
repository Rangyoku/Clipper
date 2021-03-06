from urllib2 import urlopen

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.db.models import Count
from django.contrib.auth.forms import AuthenticationForm
from django import forms

from core.models import UserProfile, Collection, Bookmark, Tag
from core.forms import CreateCollection, EditCollection, CreateBookmark, CreateBookmarklet, EditBookmark

def index(request):
    #collections_with_counts = Collection.objects.annotate(Count('bookmark'))
    #context = {'collections_with_counts': collections_with_counts}
    return render(request, 'core/index.html')

def home(request):
    """ The home view for a logged in user. """
    user_collections = Collection.objects.filter(user=request.user)
    user_bookmarks = Bookmarks.objects.filter(user=request.user)
    return render(request, 'core/home.html', {'user_collections': user_collections, 'user_bookmarks': user_bookmarks})

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

def collection_create(request):
    """ Create a new collection. """
    if request.method == 'POST': # If the form has been submitted...
        form = CreateCollection(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            is_private = form.cleaned_data['is_private']
            userprofile = request.user.userprofile
            
            new_collection = Collection(name=name, description=description, is_private=is_private, user=userprofile)
            new_collection.save()
            
            return HttpResponseRedirect('/home/') # Redirect after POST
    else:
        form = CreateCollection() # An unbound form

    return render(request, 'core/collection_create.html', {
        'form': form,
    })

def collection_detail(request, collection_id):
    """ View the details of one collection. """
    collection = get_object_or_404(Collection, pk=collection_id)
    return render(request, 'core/collection_detail.html', {'collection': collection})

def collection_edit(request, collection_id):
    """ Edit the detials of one collection. """
    collection = get_object_or_404(Collection, pk=collection_id)
    if request.method == 'POST': # If the form has been submitted...
        form = EditCollection(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            collection.name = form.cleaned_data['name']
            collection.description = form.cleaned_data['description']
            collection.is_private = form.cleaned_data['is_private']

            collection.save() # Save the new collection info.
            
            return HttpResponseRedirect(reverse('core:collection_detail', args=[collection.id])) # Redirect after POST
    else:
        form = EditCollection(initial={'name': collection.name, 'description': collection.description, 'is_private': collection.is_private}) # An unbound form

    return render(request, 'core/collection_edit.html', {
        'collection': collection, 'form': form,
    })
    
def bookmark_create(request):
    """ Create a new bookmark within the collection ID provided. --- Change it to not provided for now"""
    #collection = get_object_or_404(Collection, pk=collection_id)
    if request.user.is_authenticated():
        if request.method == 'POST': # If the form has been submitted...
            form = CreateBookmark(request.POST) # A form bound to the POST data
            if form.is_valid(): # All validation rules pass
                name = form.cleaned_data['name']
                url = form.cleaned_data['url']
                is_private = form.cleaned_data['is_private']
                read_later = form.cleaned_data['read_later']
                rating = form.cleaned_data['rating']
                notes = form.cleaned_data['notes']
                collection = form.cleaned_data['collection']
                userprofile = request.user.userprofile
            
                get_url = urlopen(url) # Opens a connection to the bookmark's url
                raw_html = get_url.read() # Reads that connection into raw_html to be saved.
                get_url.close() # Closes the connection.

                new_bookmark = Bookmark(name=name, is_private=is_private, url=url, read_later=read_later,
                    collection=collection, rating=rating, notes=notes, raw_html=raw_html, user=userprofile)
                new_bookmark.save()

                return HttpResponseRedirect(reverse('core:bookmark_detail', args=[new_bookmark.id])) # Redirect after POST
        else:
            form = CreateBookmark(request.user) # An unbound form
            return render(request,'core/bookmark_create.html',{'form':form})

        """return render(request, 'core/bookmark_create.html', {
            'form': form
            })            """
        
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form':form})

def bookmarklet_create(request):
    """ Create a new bookmark within the collection ID provided. --- Change it to not provided for now"""
    #collection = get_object_or_404(Collection, pk=collection_id)
    if request.user.is_authenticated():

        if request.method == 'POST': # If the form has been submitted...
            form = CreateBookmarklet(request.POST) # A form bound to the POST data
            if form.is_valid(): # All validation rules pass
                name = form.cleaned_data['name']
                url = form.cleaned_data['url']
                is_private = form.cleaned_data['is_private']
                read_later = form.cleaned_data['read_later']
                rating = form.cleaned_data['rating']
                notes = form.cleaned_data['notes']
                collection = form.cleaned_data['collection']
                userprofile = request.user.userprofile
                
                raw_html = ''
                if read_later:
                    get_url = urlopen(url) # Opens a connection to the bookmark's url
                    raw_html = get_url.read() # Reads that connection into raw_html to be saved.
                    get_url.close() # Closes the connection.

                new_bookmark = Bookmark(name=name, is_private=is_private, url=url, read_later=read_later, collection=collection, rating=rating, notes=notes, raw_html=raw_html, user=userprofile)
                new_bookmark.save()
                
                return HttpResponseRedirect(reverse('core:bookmark_detail', args=[new_bookmark.id]) ) # Redirect after POST
            else: 
                """If NOT form.is_valid()"""
                errors = "please fix errors"
                #form = CreateBookmarklet(user=request.user, initial={'url': url, 'name': title}) # An unbound form
                #form.fields['url'].widget = forms.HiddenInput()
                #form = CreateBookmarklet(request.user)
                return render(request,'core/bookmarklet_create.html',{'form':form, 'errors': errors})
        else:
            data = request.GET.copy()
            url = data['url']
            title = data['title']
            form = CreateBookmarklet(user=request.user, initial={'url': url, 'name': title}) # An unbound form
            form.fields['url'].widget = forms.HiddenInput()
            #form = CreateBookmarklet() #An unbound form
            return render(request,'core/bookmarklet_create.html',{'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form':form})

        
def bookmark_detail(request, bookmark_id):
    """ View the details of one bookmark. """
    bookmark = get_object_or_404(Bookmark, pk=bookmark_id)
    return render(request, 'core/bookmark_detail.html', {'bookmark': bookmark})

def bookmark_edit(request, bookmark_id):
    """ Edit the detials of one bookmark. """
    bookmark = get_object_or_404(Bookmark, pk=bookmark_id)
    if request.method == 'POST': # If the form has been submitted...
        form = EditBookmark(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            bookmark.name = form.cleaned_data['name']
            bookmark.url = form.cleaned_data['url']
            bookmark.is_private = form.cleaned_data['is_private']
            bookmark.read_later = form.cleaned_data['read_later']
            bookmark.rating = form.cleaned_data['rating']
            bookmark.notes = form.cleaned_data['notes']
            bookmark.collection = form.cleaned_data['collection']

            bookmark.save() # Save the new collection info.

            return HttpResponseRedirect(reverse('core:bookmark_detail', args=[bookmark.id])) # Redirect after POST
    else:
        form = EditBookmark(initial={'name': bookmark.name, 'is_private': bookmark.is_private, 'url': bookmark.url,
               'read_later':bookmark.read_later, 'rating': bookmark.rating, 'notes': bookmark.notes}) # An unbound form

        return render(request, 'core/bookmark_edit.html', {
              'bookmark': bookmark, 'form': form })

def bookmark_viewhtml(request, bookmark_id):
    """ View the raw HTML for this bookmark"""
    bookmark = get_object_or_404(Bookmark, pk=bookmark_id)
    return render(request, 'core/bookmark_viewhtml.html', {'bookmark': bookmark})