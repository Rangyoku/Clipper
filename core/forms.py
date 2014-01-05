from django import forms

class CreateCollection(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(max_length=350)
    is_private = forms.BooleanField(required=False)

class EditCollection(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(max_length=350)
    is_private = forms.BooleanField(required=False)


class CreateBookmark(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    url = forms.URLField(max_length=500, required=True)
    is_private = forms.BooleanField(required=False)
    rating = forms.IntegerField(required=False)
    notes = forms.CharField(max_length=500, required=False)
    # collection = models.ForeignKey(Collection)

class EditBookmark(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    url = forms.URLField(max_length=500, required=True)
    is_private = forms.BooleanField(required=False)
    rating = forms.IntegerField(required=False)
    notes = forms.CharField(max_length=500, required=False)
    # collection = models.ForeignKey(Collection)