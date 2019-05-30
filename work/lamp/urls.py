from django.conf.urls import url
from . import models,views

app_name= 'lamp'



urlpatterns = [


    url(r'^single/(\d+)/$', views.Single.as_view(), name='single'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^accountl/$', views.Accountl.as_view(), name='accountl'),
    url(r'^activation/(.*?)/$', views.Activation.as_view(), name='activation'),
    url(r'^product/$', views.Product.as_view(), name='product'),
    url(r'^checkout/$', views.Checkout.as_view(), name='checkout'),


    url(r'^ajaxurl/(\d+)/$', views.Ajaxurl.as_view(), name='ajaxurl'),



    url(r'', views.Index.as_view(), name='index'),





]
