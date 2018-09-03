import pytest
from django.contrib.auth.models import User

from crud.tests.factories import UserProfileFactory


@pytest.fixture()
def user(db):
    return UserProfileFactory.create()


@pytest.fixture()
def superuser(db):
    admin = User.objects.create_user("admin", "admin@test.com", "admin123")
    admin.is_staff = True
    admin.save()
    return admin
