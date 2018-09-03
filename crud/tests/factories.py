import factory
from crud.models import UserProfile


class UserProfileFactory(factory.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    class Meta:
        model = UserProfile
