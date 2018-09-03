import factory
from django.contrib.auth.models import User
from crud.models import UserProfile


class AdminUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User


class UserProfileFactory(factory.django.DjangoModelFactory):
    owner = factory.SubFactory(AdminUserFactory)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    class Meta:
        model = UserProfile
