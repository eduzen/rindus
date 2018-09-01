from django.conf.urls import url, include
from django.contrib.auth import views
from crud.views import home


urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^$', home, name='home'),
]
