from django.conf.urls import url
from views import *

urlpatterns = [
	url(r'^$', index),
	url(r'^testimonials/$', testimonials),
	url(r'^about/$', about),
	url(r'^projects/$', projects)
]