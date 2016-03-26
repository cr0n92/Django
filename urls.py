from django.conf.urls import url, include
from givmed import views
from rest_framework import serializers



urlpatterns = [
	#url(r'^userades/$', views.users_list),
	#url(r'^info/$', views.info_list),
	url(r'^med_delete/(?P<barcode>[0-9]+)/$', views.med_del),
	url(r'^med_check/(?P<phone>[0-9]+)/$', views.med_check),
	url(r'^med/(?P<phone>[0-9]+)/$', views.med_detail),
	url(r'^needs/$', views.NeedsList.as_view()),
	url(r'^reg/$', views.user_register),
	url(r'^verify/$', views.otp_verify),
	url(r'^ios-needs/$', views.NeedsListIOS.as_view()),
	url(r'^pharm-detail/(?P<pharmacyPhone>[0-9]*)/$', views.PharmacyDetail.as_view()),
	url(r'^user-detail/(?P<userPhone>[0-9]*)/$', views.UserDetail.as_view()),









]