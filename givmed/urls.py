from django.conf.urls import url, include
from givmed import views
from rest_framework import serializers



urlpatterns = [
	#url(r'^userades/$', views.users_list),
	#url(r'^med/$', views.med_list),
	#url(r'^info/$', views.info_list),
	url(r'^med/$', views.MedList.as_view()),
	url(r'^need/$', views.NeedsList.as_view()),
	url(r'^reg/$', views.user_register),





]