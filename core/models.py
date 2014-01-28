# Create your models here.
from django.db import models
import datetime
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    #date_joined = models.DateTimeField('date joined',  default=timezone.now)

    def create_user_profile(sender, instance, created, **kwargs):
        #The method get_profile() does not create a profile if one does not exist. 
        #Need to register a handler
        if created:
	        UserProfile.objects.create(user=instance)
    post_save.connect(create_user_profile, sender=User)
	
    def __unicode__(self):
		return str(self.user)
    def email_user(self, subject, message, from_email=None):
        #Sends an email to this User.
        send_mail(subject, message, from_email, [self.email])

class Collection(models.Model):
    name = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=350, blank=True)
    is_private = models.BooleanField(default=False)
    user = models.ForeignKey(UserProfile) #test change userprofile to bookmark

    def bookmark_count(self):
		return str(self.bookmark_set.count())
		
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('core:collection_detail', args=[str(self.id)])
    
    def __unicode__(self):
		return self.name

class Bookmark(models.Model):
    name = models.CharField(max_length=30, blank=False)
    url = models.URLField(max_length=500, blank=False)
    date_added = models.DateField(auto_now_add=True)
    cache_content = models.TextField(blank=True)
    is_private = models.BooleanField(default=False)
    rating = models.IntegerField(blank=True)
    notes = models.CharField(max_length=500, blank=True)
    user = models.ForeignKey(UserProfile)
    collection = models.ForeignKey(Collection)

	
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('core:bookmark_detail', args=[str(self.id)])
		    
    def __unicode__(self):
		return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30, blank=False)
    
    def __unicode__(self):
		return self.name

