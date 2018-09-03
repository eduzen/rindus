# users/forms.py
from django import forms

from crud.models import UserProfile

# from localflavor.generic.forms import IBANFormField


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"
