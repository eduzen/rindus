from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from crud.models import UserProfile
from crud.forms import UserProfileForm


class UserListView(LoginRequiredMixin, generic.ListView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = UserProfile
    # queryset = Post.objects.published()
    context_object_name = "users"
    template_name = "crud/home.html"
    paginate_by = 5
    ordering = ["id"]


class UserCreate(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = UserProfile
    fields = ["first_name", "last_name", "iban"]
    success_url = reverse_lazy("user-list")


class UserUpdate(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = UserProfile
    form_class = UserProfileForm
    success_url = reverse_lazy("user-list")


class UserDelete(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = UserProfile
    success_url = reverse_lazy("user-list")
