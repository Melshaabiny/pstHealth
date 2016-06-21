from django.conf.urls import url
from . import views
from home import views as home_views

urlpatterns = [
	url(r'^$', home_views.index, name='index'),
	url(r'^about/$', home_views.about, name='about'),
]