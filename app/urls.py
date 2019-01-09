from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
       url(r'^$',views.home,name='Home'),
       url(r'^new_neighbourhood',views.new_neighbourhood,name='new_neighbourhood'),
       url(r'^detail/(?P<neighbourhood_id>\d+)/$' , views.neighbourhood_details, name='detail' ),
       url(r'^profile/',views.profile, name='profile'),
       url(r'^new/profile$', views.new_profile, name='new-profile'),
