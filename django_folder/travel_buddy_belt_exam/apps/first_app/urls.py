from django.conf.urls import url
from . import views
from views import *

urlpatterns = [
	url(r'^$', index),
	url(r'^travels$', travels),
	url(r'^travels/destination/7$', destination_seven),
	url(r'^travels/add$', add),
]