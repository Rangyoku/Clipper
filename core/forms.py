from django import forms
from core.models import UserProfile, Collection, Bookmark

class CreateCollection(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(max_length=350)
    is_private = forms.BooleanField(required=False)

class EditCollection(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(max_length=350)
    is_private = forms.BooleanField(required=False)

class CreateBookmark(forms.ModelForm):
    class Meta:
        model = Bookmark
        exclude = ['cache_content', 'raw_html', 'user']

    def __init__(self, user, *args, **kwargs):
            super(CreateBookmark, self).__init__(*args, **kwargs)
            self.fields['collection'].queryset = Collection.objects.filter(user=user)

class CreateBookmarklet(forms.ModelForm):
    class Meta:
        model = Bookmark
        exclude = ['cache_content', 'raw_html', 'user']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CreateBookmarklet, self).__init__(*args, **kwargs)
        self.fields['collection'].queryset = Collection.objects.filter(user=user)

class EditBookmark(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    url = forms.URLField(max_length=500, required=True)
    is_private = forms.BooleanField(required=False)
    read_later = forms.BooleanField(required=False)
    rating = forms.IntegerField(required=False)
    notes = forms.CharField(max_length=500, required=False)
    collection = forms.ModelChoiceField(queryset = Collection.objects.all(), required=False)
    # collection = models.ForeignKey(Collection)