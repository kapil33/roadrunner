from django.conf.urls import url
from epay import views
urlpatterns = [
	url(r'^pay-now/',views.pay_now ,name="pay_now"),
	url(r'^pay-later/',views.pay_later ,name="pay_later"),
	url(r'^add-wallet/',views.add_allet ,name="add-wallet"),
]

