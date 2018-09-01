from django.contrib.auth.models import User, Group
from django.shortcuts import render


def home(request):
	return render(request, 'crud/home.html')
