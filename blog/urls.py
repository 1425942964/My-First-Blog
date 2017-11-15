from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$', views.introduction, name='introduction'),
	url(r'^posts/', views.post_list, name='posts'),
	url(r'^contact/', views.contact, name='contact')
]