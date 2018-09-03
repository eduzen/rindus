from django.db import models
from django.contrib.auth.models import User

from localflavor.generic.models import IBANField


class UserProfile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    iban = IBANField()

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"

