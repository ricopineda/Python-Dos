from django.conf.urls import url
from . import views           
urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
	url(r'^home$', views.home),
	url(r'^add$', views.add),
	url(r'^add_list$', views.add_list),
	url(r'^view$', views.view),
	url(r'^delete(?P<id>\d+)$', views.delete),
]
