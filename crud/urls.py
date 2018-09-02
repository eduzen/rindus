from django.conf.urls import url, include
from django.contrib.auth import views
from crud.views import home


urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^accounts/', include('allauth.urls')),

    url(r'^$', home, name='home'),
]
