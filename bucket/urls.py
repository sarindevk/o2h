from django.conf.urls import url
from . import views


urlpatterns = [
#	 url(r'^refresh_cart/$', views.clear_cart, name='clear_cart'),
#	 url(r'^view_cart/$', views.view_cart, name='view_cart'),
#	 url(r'^add_to_cart/$', views.add_to_cart, name='addtocart'),    
    url(r'^$', views.index, name='index'),
    
]