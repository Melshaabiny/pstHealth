from django.conf.urls import url
from . import views
from fitness import views as fitness_views

urlpatterns = [
	url(r'^fitness$', fitness_views.renderFit, name='fitness'),
]