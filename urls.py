from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('core.urls', namespace='core')),
	url(r'^accounts/register/$',
	        RegistrationView.as_view(form_class=RegistrationFormUniqueEmail),
	        name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'', include('social_auth.urls')),#Login via Facebook, Twitter and Google
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

