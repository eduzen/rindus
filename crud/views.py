from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from crud.models import UserProfile
from crud.forms import UserProfileForm


class UserListView(generic.ListView):
    model = UserProfile
    # queryset = Post.objects.published()
    context_object_name = "users"
    template_name = "crud/home.html"
    paginate_by = 5
    ordering = ["id"]


class UserCreate(CreateView):
    model = UserProfile
    fields = ['first_name', 'last_name', 'iban']
    success_url = reverse_lazy('user-list')


class UserUpdate(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    success_url = reverse_lazy('user-list')


class UserDelete(DeleteView):
    model = UserProfile
    success_url = reverse_lazy('user-list')
