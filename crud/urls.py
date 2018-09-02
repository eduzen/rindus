from django.conf.urls import url, include
from django.contrib.auth import views
from crud.views import UserListView, UserCreate, UserDelete, UserUpdate
from django.urls import path

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^accounts/', include('allauth.urls')),
    path('user/add/', UserCreate.as_view(), name='user-add'),
    path('user/<int:pk>/', UserUpdate.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', UserDelete.as_view(), name='user-delete'),
    path('user/', UserListView.as_view(), name='user-list'),
    url(r'^$', UserListView.as_view(), name='home'),
]
